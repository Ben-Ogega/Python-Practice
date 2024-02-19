def is_palindrome(text: str) -> bool:
    """
    Checks if a text text is a palindrome, considering:

    - Ignoring punctuation and preserving spaces
    - Capitalizing the first letter
    - Handling only odd-length strings

    Args:
        text (str): The text text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.

    >>> is_palindrome("noon")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("dented")
    False
    >>> is_palindrome("Was it a car or a cat I saw?")
    True
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    """
    # Remove all non-alphanumeric characters and make the text lowercase
    text = ''.join(c for c in text if c.isalnum()).lower()

    # Check if the text is the same forwards and backwards
    return text == text[::-1]



