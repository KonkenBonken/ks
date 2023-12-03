from subprocess import run as process


def run(script: str, *input: str):
    return process(
        ['py', 'ks.py', f'tests/{script}.ks'],
        input='\n'.join(input),
        capture_output=True,
        text=True
    ).stdout.strip()


def test(script: str, input: 'tuple[str]', expected: str):
    output = run(script, *input)
    if output == expected:
        print(script, 'succeeded')
    else:
        print('\n{script} failed')
        print({'expected': expected,
               'recieved': output})


test('let', '', "{'A': True, 'B': 123, 'C': 12.3}")
test('prompt', ('1', '5'), "A: B: True\n5")
