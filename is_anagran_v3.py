'''

'''
import pytest

def is_anagram_v3(s1: str, s2: str) -> bool:
    # convert the input string to lowercase for case-insenstive comparison
    s1 = s1.lower()
    s2 = s2.lower()
    # Remove the spaces and sort the characters in both strings
    s1_sorted = ''.join(sorted(s1.replace(' ', '')))
    s2_sorted = ''.join(sorted(s2.replace(' ', '')))

    # compare the sorted strings
    return s1_sorted == s2_sorted

@pytest.mark.parametrize("s1, s2, expected", [
    ('Astronomer', 'Moon starer', True),
    ('bear', 'breach', False),
    ('Dormitory', 'Dirty room', True),
    ('python', 'java', False),
    ('William Shakespeare', 'I am a wise phrase maker', False)
])
def test_anagram(s1, s2, expected):
    assert is_anagram_v3(s1, s2) == expected
