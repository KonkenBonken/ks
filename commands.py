varnames = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
variables = dict()


def Let(line: str):
    datatype = line[1]
    varname = line[2]
    value = line[3:]

    assert varname in varnames

    if datatype == 'β':
        assert value in {'0', '1'}
        variables[varname] = True if value == '1' else False
    elif datatype == 'Ε':
        variables[varname] = int(value)
    elif datatype == 'ε':
        variables[varname] = float(value)


commands = {
    '∃': Let
}
