from utils import Plasmid, Sequence
from typing import List


def findPAMIndices(sequence: Sequence) -> List[int]:
    """returns a list of indices for all possible PAM in the given sequence"""
    indices = []
    i = 0 if isinstance(sequence, Plasmid) and sequence.circular else 16

    while i < len(sequence):
        nextIndex = sequence.sequence.index("GG", i)
        indices += [nextIndex]
        i = nextIndex + 1

    i = 0

    while i < len(sequence) - (
        0 if isinstance(sequence, Plasmid) and sequence.circular else 16
    ):
        nextIndex = sequence.sequence.index("CC", i)
        indices += [nextIndex]
        i = nextIndex + 1

    return indices


def findGuideRNAs(sequence: Sequence) -> List[str]:
    """returns a list of all possible sgRNAs in the given sequence"""
    import re
    from re import Match

    matches: Match | None = re.match("([ATCG]{16}GG)|(CC[ATCG]{16})", sequence.sequence)

    return [match for match in matches] if matches else []
