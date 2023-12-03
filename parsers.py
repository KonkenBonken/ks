from charsets import varnames, datatypes

def varparser(datatype: str, value: str):
    assert datatype in datatypes
    
    if datatype == 'β':
        assert value in {'0', '1'}
        return True if value == '1' else False
    elif datatype == 'ι':
        return int(value)
    elif datatype == 'ζ':
        return float(value)
    else:
        raise 'unknown datatype'
