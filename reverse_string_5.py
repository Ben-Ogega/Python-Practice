def reverse_string_v5(s):
    """
    Reverse the given string using a temporary list.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_string_v5("hello")
        'olleh'
    """
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)
