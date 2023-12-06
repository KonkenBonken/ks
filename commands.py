from parsers import expressionparser
from charsets import varnames, datatypes
from variables import variables

def Let(line: str):
    datatype = line[1]
    varname = line[2]
    value = line[3:]

    assert varname in varnames

    variables[varname] = expressionparser(datatype + value)


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
            print(expressionparser(line[i:]))
            break


def Vardump(_):
    print(variables)


def Goto(line:str):
    return expressionparser(line[1:])
    

commands = {
    '∃': Let,
    'ω': Prompt,
    'Ψ': Print,
    'Ω': Vardump,
    'Δ': Goto
}
