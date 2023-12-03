from subprocess import run as process


def run(script: str, *input: str):
    return process(
        ['py', 'ks.py', f'tests/{script}.ks'],
        input='\n'.join(input),
        capture_output=True,
        text=True
    ).stdout.strip()


def test(script: str, input: 'tuple[str]', expected: str):
    expected = expected.replace('⏎', '\n')
    output = run(script, *input)
    if output == expected:
        print(script, 'succeeded')
    else:
        print('\n{script} failed')
        print({'expected': expected,
               'recieved': output})


test('let', '', "{'A': True, 'B': 123, 'C': 12.3}")
test('prompt', ('1', '5'), "A: B: True⏎5")
test('print', '', "5⏎3.1⏎2⏎False⏎2⏎False⏎2⏎5")
test('operations', '', "5⏎8⏎8.2⏎10.2⏎2⏎1.8⏎6.8⏎15⏎7.5⏎2.0⏎7.5")
