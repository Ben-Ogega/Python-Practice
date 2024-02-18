def reverse_string_v4(s):
    """
        Reverse the given string using the built-in 'reversed' function and 'join'.

        Args:
            s (str): The input string to be reversed.

        Returns:
            str: The reversed string.

        Examples:
            >>> reverse_string_v4("hello")
            'olleh'
        """
    s1 = "".join(reversed(s))
    return  s1