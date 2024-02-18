def reverse_string_v3(s):
    """
    Reverse the given string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_string_v3("hello")
        'olleh'
    """
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]  # Append characters from s to s1
        length = length - 1
    return s1
