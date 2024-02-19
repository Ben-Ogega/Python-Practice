'''
     The basic idea is that sometimes people's bodies produce too much of a given protein.
     That can cause all sorts of havoc.

    But if you can create a very specific molecule (called a micro-RNA),
    it can prevent the protein from being produced.
    This process is called RNA Interference
    This exercise is adapted from Exercism website
'''
def to_rna(dna_strand: str) -> str:

    """
    Returns the transcribed RNA strand else raises and error

    Transcribes a DNA strand into an RNA strand

    The four nucleotides found in DNA are adenine(A), cystosine(C), guanine(G), and thymine(T)

    The four nucleotides found in RNA are adenine(A), cystosine(C), guanine(G), and uracil(U)
    >>> to_rna('ATCG')
    'UAGC'
    >>> to_rna("GCTA")
    'CGAU'
    >>> to_rna("ACGT")
    'UGCA'
    >>> to_rna("")
    ''
    >>> to_rna('AAACCCGGGTTT')
    'UUUGGGCCCAAA'

    >>> to_rna('ATCGTAGC')
    'UAGCAUCG'
    >>> to_rna('gcatact')
    'CGUAUGA'
    >>> to_rna(AGTXCZY)
    'UCAG'
    """

    transcription_map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    # use a list compresion to transcribe each nucleotide
    try:
        rna_strand = ''.join(transcription_map.get(nucleotide, '') for nucleotide  in dna_strand.upper())

        return rna_strand.strip()
    except KeyError as e:
        raise ValueError("Invalid DNA strand!")
