def is_palindrome_v1(str) -> bool:
    """
    Returns True if and only is s is a palindrome
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    return reverse_string(s) == s
def reverse_string(str) -> str:
    """
    Returns a reversed version of s
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('bomob')
    'bomob'
    >>> reverse_string('dented')
    'detned'
    """

    rev = ''
    # for each character in s, add that character to the beginning of the rev accumualtor
    for ch in s:
        rev = ch + rev

    return rev