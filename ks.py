from sys import argv
from commands import commands
from charsets import commandset


file_name = argv[1]
file = open(file_name, "r", encoding="utf8")
code = file.read()
file.close()

for line in code.replace('⋮', '\n').split('\n'):
    if len(line) == 0:
        continue

    assert line[0] in commandset

    command = commands.get(line[0])
    command(line.split()[0])
