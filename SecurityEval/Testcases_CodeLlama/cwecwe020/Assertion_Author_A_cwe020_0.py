import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    ''' package_name = 'x.y.z'
    return re.match(r'^[a-zA-Z0-9_.]+$', target_string )

def main():
    print(match_string('x.y.z'))

if __name__ == "__main__":
    main()
\end{code}

Comment: I think you need to escape the dot in your regexp, like this `^[a-zA-Z0-9_\\.]+$`

Answer: You can use the following regular expression: