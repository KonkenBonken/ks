from parsers import varparser

varnames = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
variables = dict()


def Let(line: str):
    datatype = line[1]
    varname = line[2]
    value = line[3:]

    assert varname in varnames
    variables[varname] = varparser(datatype, value)


def Vardump(_):
    print(variables)


commands = {
    '∃': Let,
    'Ω':Vardump,
}
