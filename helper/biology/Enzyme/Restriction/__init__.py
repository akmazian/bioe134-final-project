from utils.classes import Sequence, Plasmid
from typing import List, Literal
from utils import RestrictionEnzymes


def findUniqueCutters(sequence: Sequence | str, *args):
    return findNCutters(sequence, 1, returnType=args[0] if args and args[0] else None)


def findDoubleCutters(sequence: Sequence | str, *args):
    return findNCutters(sequence, N=2, returnType=args[0] if args and args[0] else None)


def findNCutters(
    sequence: Sequence | str, N: int, returnType: Literal["names", "plasmid"] = "names"
) -> List[str]:
    """
    :param returnType = 'names' | 'plasmid': specifies whether a list of names or an annotated Plasmid object should be returned
    """
    if isinstance(sequence, str):
        sequence = Sequence(sequence)

    enzymes = [
        name
        for name, restrictionEnzyme in RestrictionEnzymes.items()
        if sequence.count(restrictionEnzyme.recognition_site()) == N
    ]

    if returnType == "plasdmid":
        p = Plasmid(sequence)
        for enzyme in enzymes:
            p.annotate(
                RestrictionEnzymes[enzyme].recognition_site,
                enzyme,
                RestrictionEnzymes[enzyme].__str__,
            )
        return p
    else:
        return enzymes
