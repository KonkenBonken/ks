from parsers import varparser
from charsets import varnames, datatypes

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
    for i in range(1, len(line)):
        if line[i] in varnames:
            print(variables[line[i]])
        elif line[i] in datatypes:
            print(varparser(line[i], line[i+1:]))
            break


def Vardump(_):
    print(variables)


commands = {
    '∃': Let,
    'ω': Prompt,
    'Ψ': Print,
    'Ω': Vardump,
}
