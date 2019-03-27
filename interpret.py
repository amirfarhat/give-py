import sys

# syntax to swap out for python3
SYNTAX_KEYWORD_MAP = {

     # synonyms for def
    'make'      : 'def',
     
     # synonyms for return
    'give'      : 'return',

     # synonyms for print
    'SHO'       : 'print',
    'SHOW'      : 'print',
    'sho'       : 'print',
    'show'      : 'print',

     # synonyms for append
    '.also'     : '.append',
    '.and'      : '.append',
    
     # synonyms for import
    'bring'     : 'import',
    'want'      : 'import',

    # give syntax we want to eliminate
    ' take ': '', 
    ' take' : ''
}

def main():
    # get .give file as first arg
    _, to_run = sys.argv

    # sanitize .give filename
    to_run = to_run.strip()

    # file must end with .give
    if not to_run.endswith('.give'):
        raise Exception("Mast ind .give pendejo")

    # open code file and interpret give to python
    with open(to_run, 'r') as code_file:
        code = code_file.read()

        # replace give keywords with python keywords
        for old, new in SYNTAX_KEYWORD_MAP.items():
            code = code.replace(old, new)
    
        # make a .py file of the give code
        with open('_temp.py', 'w+') as temp:
            temp.write(code)

main()