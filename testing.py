from subprocess import run as process


def run(script: str, *input: str):
    return process(
        ['py', 'ks.py', f'tests/{script}.ks'],
        input='\n'.join(input),
        capture_output=True,
        text=True
    ).stdout.strip()


assert run('let') == "{'A': True, 'B': 123, 'C': 12.3}"
assert run('prompt', '1', '5') == "A: B: True\n5"
