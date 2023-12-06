from sys import argv
from commands import commands
from charsets import commandset


file_name = argv[1]
file = open(file_name, "r", encoding="utf8")
code = file.read()
file.close()

i = 0
lines = code.split('\n')

while i < len(lines):
    line = lines[i]
    i += 1

    if len(line) == 0:
        continue
    if line[0] == ' ':
        continue

    for line in line.split('⋮'):
        assert line[0] in commandset

        command = commands.get(line[0])
        res = command(line.split()[0])

        if isinstance(res, (int, float)):
            i += int(res)-1
