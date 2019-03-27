import subprocess

def integration_test():
    # run bash command running the .give test file
    bash_command = 'bash give.sh do.give'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    actual, error = process.communicate()
    
    # assert no errors
    assert error is None

    # assert expected result of test file
    expected = 'We use the following list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nLength of list: 10\nSum of list: 55\nCumulative averages of list: [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]\n'
    assert str(expected) == str(actual, 'utf-8')

if __name__ == '__main__':
    integration_test()