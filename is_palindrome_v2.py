import time
def is_palindrome_v2(str)-> bool:
    """
    Returns True if and only if str is a palindrome
    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('repaper')
    True
    >>> is_palindrome_v2('madam')
    True
    >>> is_palindrome_v2('tenet')
    True
    """
    # the number of chars in s.
    n = len(str)
    # compare the first half of str to the reverse of second half
    # ommit the middle character of an odd-length string
    return str[:n//2] == reverse_string(str[n- n//2:])

def reverse_string(str)-> bool:

    """
    Returns a reversed version of str
    >>> reverse_string('noon')
    'noon'
    >>> reverse_string('repaper')
    'repaper'
    >>> reverse_string('madam')
    'madam'
    >>> reverse_string('tenet')
    'tenet'
    """
    rev = ''
    # for each character in str, add that character to the beggining of rev

    for ch in str:
        rev = ch + rev

    return rev