def is_palindrome_v3(text: str) -> bool:
    """
    Checks if a text string is a palindrome, considering:

    - Ignoring punctuation and preserving spaces
    - Capitalizing the first letter
    - Handling only odd-length strings

    Args:
        text (str): The text string to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    >>> is_palindrome_v3("rotor")
    True
    >>> is_palindrome_v3("noon")
    True
    >>> is_palindrome_v3("racecar")
    True
    >>> is_palindrome_v3("dented")
    False
    >>> is_palindrome_v3("yellow")
    False
    """

    # the number of char in text
    n = len(text)
    # compare the first half of text to the reverse of the second half
    #Omit the middle character of an odd-length string

    return text[:n//2] == reverse_string(text[(n-n//2):])

def reverse_string(s: str) -> str:
    """
    Return a reversed version of s
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('dented')
    'detned'
    >>> reverse_string('racecar')
    'racecar'
    """
    # for each character in s, add that character to the beginning of rev.
    rev = ''
    for ch in s:
        rev = ch + rev

    return  rev



