def get_commented_lines(file_name):
    '''
    This function load a file and will return an array of only
    the commented line (lines starting with '#')
    '''
    
    f = open(file_name)
    lines = f.readlines()
    commented_lines = []
    for _line in lines:
        if '#' in _line:
            commented_lines.append(_line)

    return commented_lines

def get_commented_lines_of_files(list_files):
    '''
    Return an array of all the commented lines
    '''
    
    data_commented_lines = []
    for _file in list_files:
        _commented_lines = get_commented_lines(_file)
        data_commented_lines.append(_commented_lines)
    
    return data_commented_lines
