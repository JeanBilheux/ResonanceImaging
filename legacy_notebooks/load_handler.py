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
