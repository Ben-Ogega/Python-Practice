def reverse_string_v6(s):
    """
       Reverse the given string using recursion.

       Args:
           s (str): The input string to be reversed.

       Returns:
           str: The reversed string.

       Examples:
           >>> reverse_string_v6("hello")
           'olleh'
           >>> reverse_string_v6("Dennis Ontonchi is my elder brother")
           'rehtorb dleme ym si ihcnotnO sinned'
       """
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_v6(s[:-1])

print(reverse_string_v6("Dennis Ontonchi is my elder brother"))