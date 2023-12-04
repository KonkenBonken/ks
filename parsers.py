from re import split
from charsets import varnames, datatypes, binaryoperators
from variables import variables


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


def expressionparser(expr: str):
    if expr in varnames:
        return variables[expr]

    for operators in ('+-', '×÷'):
        if any(c in expr for c in operators):
            opindex = next(i for i, c in
                           list(enumerate(expr))[::-1]
                           if c in operators)
            operator = expr[opindex]

            left, right = map(expressionparser,
                              (expr[:opindex], expr[opindex+1:]))

            if operator == '×':
                return left * right
            elif operator == '÷':
                return left / right
            elif operator == '+':
                return left + right
            elif operator == '-':
                return left - right

    if expr[0] in datatypes:
        return varparser(expr[0], expr[1:])
