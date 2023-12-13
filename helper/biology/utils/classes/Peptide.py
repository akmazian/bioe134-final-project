from typing import List, SupportsIndex
from .AminoAcid import AminoAcid
from .Sequence import Sequence


class Peptide(Sequence):
    unitType = AminoAcid

    def __init__(self, sequence: List[unitType] = []) -> None:
        self.sequence = sequence
