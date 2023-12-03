from parsers import varparser

varnames = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
variables = dict()


def Let(line: str):
    datatype = line[1]
    varname = line[2]
    value = line[3:]

    assert varname in varnames
    variables[varname] = varparser(datatype, value)


def Prompt(line: str):
    for i in range(1, len(line), 2):
        datatype = line[i]
        varname = line[i+1]

        value = input(varname + ': ')
        Let(f'∃{datatype}{varname}{value}')


def Print(line: str):
    for varname in line[1:]:
        print(variables[varname])


def Vardump(_):
    print(variables)


commands = {
    '∃': Let,
    'ω': Prompt,
    'Ψ': Print,
    'Ω': Vardump,
}
