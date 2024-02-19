
"""
    Author: Benard N. Ogega
    Location: Kisumu - Kenya
    Date: 2024/02/19
    
    Classic Anagrams:
        Listen -> Silent
        Race -> Care
        God -> Dog
        Cinema -> Iceman
        Dormitory -> Dirty room
        Astronomer -> Monstrous area
        The Morse Code -> Here come dots
        A gentleman -> Elegant man
    Punny Anagrams:
        Debit card -> Bad credit
        Vacation -> Avoidcation
        Election -> Lies on
        Silence -> Listen
        Astronomer -> Moon starer
        Schoolmaster -> As cool as them
        Conversation -> No reservation
        A decimal point -> I'm a dot in place
    Famous Anagrams:
        William Shakespeare -> I am a wise phrase maker
        Silent -> Listen
        Clint Eastwood -> Old west action
        Are we not drawn onward to new era -> A war to drown out, are we not near an end? (Winston Churchill)
        Eleven plus two -> Twelve plus one
    Challenging Anagrams:
        Resigned -> Singe red
        Anguish -> Guinea
        Astronomer -> Moon starer
        Eleven plus two -> Twelve plus one
        Indecision -> Decide on
"""

import unittest
def is_anagram_v2(s1: str, s2:str)-> bool:

    """
    Checks if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """


    # convert the input string to lowercase for case-insenstive comparison
    s1 = s1.lower()
    s2 = s2.lower()
    # Remove the spaces and sort the characters in both strings
    s1_sorted = ''.join(sorted(s1.replace(' ', '')))
    s2_sorted = ''.join(sorted(s2.replace(' ', '')))

    # compare the sorted strings
    return  s1_sorted == s2_sorted

class TestIsAnagram(unittest.TestCase):
    def test_anagram_1(self):
        self.assertTrue(is_anagram_v2("Astronomer", "Moon starer"))

    def test_anagram_2(self):
        self.assertFalse(is_anagram_v2("bear", "breach"))

    def test_anagram_3(self):
        self.assertTrue(is_anagram_v2("Dormitory", "Dirty room"))

    def test_anagram_4(self):
        self.assertFalse(is_anagram_v2("python", "java"))

    def test_anagram_5(self):
        self.assertTrue(is_anagram_v2('William Shakespeare', 'I am a wise phrase maker'))


if __name__ == '__main__':
    unittest.main()


