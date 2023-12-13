from ..constants.maps import NucleotideComplimentaryMap as comp


def revcomp(sequence: str, reversed: bool = True) -> str:
    """
    @param reversed - pass in False to optional second param to get complementary strand 3' to 5'
    @return the reverse complement of the provided sequence 5' to 3'
    """
    revcomp = ""

    for base in sequence.upper():
        revcomp += comp[base]

    return revcomp[::-1] if reversed else revcomp
