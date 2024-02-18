# using bitwise Manipulation

def reverse_string_v2(s):
    """
    (str) -> str
    return a reversed version of the string using bitwise manipulation
    >>> reverse_string_v2("hello")
    'olleh'

    >>> reverse_string_v2('a')
    'a'
    >>> reverse_string_v2('dented')
    'detned'
    """
    return s[::-1]



print(reverse_string_v2('My car is yellow in colour'))