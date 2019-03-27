import sys

# syntax to swap out for python3
SYNTAX_KEYWORD_MAP = {
    'make'      : 'def',
    'give'      : 'return',

     # synonyms for print
    'SHO'       : 'print',
    'SHOW'      : 'print',
    'sho'       : 'print',
    'show'      : 'print',

    '.also'     : '.append',
    'bring'     : 'want',

    ' take ': '', 
    ' take' : ''
}

if __name__ == '__main__':
    _, to_run = sys.argv

    # file must end with .give
    if not to_run.endswith('.give'):
        raise Exception("Mast ind .give pendejo")

    # open code file and interpret give to python
    with open(to_run, 'r') as code_file:
        code = code_file.read()

        # replace give keywords with python keywords
        for old, new in SYNTAX_KEYWORD_MAP.items():
            code = code.replace(old, new)
    
        # print(code)

        # make a .py file of the give code
        with open('given.py', 'w') as given:
            given.write(code)