def varparser(datatype: str, value: str):
    if datatype == 'β':
        assert value in {'0', '1'}
        return True if value == '1' else False
    elif datatype == 'Ε':
        return int(value)
    elif datatype == 'ε':
        return float(value)
    else:
        raise 'unknown datatype'
