def to_rna(sequence):
    """
    Transcribes a DNA sequence into its corresponding RNA sequence.

    The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G), and thymine (T).
    The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G), and uracil (U).

    Args:
        sequence (str): The DNA sequence to be transcribed.

    Returns:
        str: The transcribed RNA sequence.

    Examples:
        >>> to_rna("G")
        'C'
        >>> to_rna("GCAT")
        'CGUA'
        >>> to_rna("AAACCCGGGTTT")
        'UUUGGGCCCAAA'
        >>> to_rna("ATCGTAGC")
        'UAGCAUCG'
        >>> to_rna("gcatact")
        'CGUAUGA'
        >>> to_rna("AGTXCZY")
        'UCAG'
    """
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''
    for letter in sequence.upper():
        rna += translations.get(letter, '')  # Use get() to handle invalid characters
    return rna