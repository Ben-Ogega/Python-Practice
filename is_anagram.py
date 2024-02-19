
'''
    Author: Ben N. Ogega
    Location: Kisumu - Kenya.
    Date: 2024-02-19
'''
def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

        >>> is_anagram('bear', 'breach')
        False
        >>> is_anagram('debit card', 'bad credit')
        True
        >>> is_anagram('python', 'java')
        False
        >>> is_anagram('Dormitory', 'Dirty room')
        True
        >>> is_anagram("silent", "listen")
        True
    """
    # convert the input string to lowercase for case-insenstive comparison
    s1 = s1.lower()
    s2 = s2.lower()
    # Remove the spaces and sort the characters in both strings
    s1_sorted = ''.join(sorted(s1.replace(' ', '')))
    s2_sorted = ''.join(sorted(s2.replace(' ', '')))

    # compare the sorted strings
    return  s1_sorted == s2_sorted
print(is_anagram('Dormitory', 'Dirty room'))