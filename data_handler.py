import pandas as pd

def load_data(list_files):
    
    data = []
    for _file in list_files:        
        _data = pd.read_csv(_file, comment='#')
        data.append(_data)
    return data
