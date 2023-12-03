from sys import argv
from commands import variables, commands

file_name = argv[1]
file = open(file_name, "r", encoding="utf8")
code = file.read()
file.close()

for line in code.split('\n'):
    if len(line) == 0:
        continue
    command = commands.get(line[0])
    command(line)
