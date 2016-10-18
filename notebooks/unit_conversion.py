def convert_ev_to_lambda(dictionary):
    new_dict = {}
    for _tag, _value_ev in dictionary.items():
        _val1 = _value_ev * 1e3
        _val2 = 81.8 / _val1
        new_val = math.sqrt(_val2)
        new_dict[_tag] = new_val
    return new_dict