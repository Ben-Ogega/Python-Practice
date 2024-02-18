def reverse_string_v1(s):
    """
    (str) -> str
    Return a reversed version of s
    >>> reverse_string_v1("hello")
    'olleh'

    >>> reverse_string_v1('a')
    'a'
    >>> reverse_string_v1('dented')
    'detned'
    """
    rev = ' ' # a string accumulator
    # for each character in s, add that character to the beginning of rev

    for char in s:
        rev = char + rev

    return rev.strip() # Remove leading and trailing whitespaces
reversed_str = reverse_string_v1("hello")
print(reversed_str)