import os
import pyfits
from PIL import Image
import numpy as np


def load_data(file_name):
    '''
    load the various file_name format
    '''
    data_type = get_data_type(file_name)
    if data_type == '.fits':
        hdulist = pyfits.open(file_name)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        return _image
    
    elif (data_type == '.tif') or (data_type == '.tiff'):
        _image = Image.open(file_name)
        _image = np.asarray(_image)
        return _image
    
    else:
        raise NotImplementedError
    
    
def get_data_type(file_name):
    '''
    using the file name extension, will return the type of the data
    
    Arguments:
        full file name
        
    Returns:
        file extension    ex:.tif, .fits
    '''
    filename, file_extension = os.path.splitext(file_name)
    return file_extension.strip()

def load_csv_table_file(file_name):
    '''
    load a csv file

    ex:
    # metadata 1
    # metadata 2
    var1, val1, val2, val3
    var2, val3, val4, val5

    will return a dictionary of the metadata and values

    {'metadata': ['metadata1','metadata2'],
    'data': {'var1': ['val1','val2','val3'],
             'var2': ['val3','val4','val5']}
             }
    '''
    if not os.path.isfile:
        raise IOError ("File does not exist!")

    _metadata = []
    _data = {}
    with open(file_name) as f:
        for line in f:
            li = line.strip()
            if li.startswith('#'):
                _metadata.append(li)
            else:
                _data_line = li.split(',')
                if len(_data_line)>1:
                    _data_float = [float(value) for value in _data_line[1:]]
                    _data[_data_line[0]] = _data_float

    result = {'metadata': _metadata,
              'data': _data}

    return result

    
