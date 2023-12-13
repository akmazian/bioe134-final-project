from __future__ import annotations
from typing import Dict, Tuple
from .Sequence import Sequence


class Plasmid(Sequence):
    def __init__(self, sequence, circular: bool = True) -> None:
        self.sequence = sequence
        self.annotations: Dict[str, Tuple[str, str]] = {}
        self.circular = circular

    def annotate(self, sequence: str, label: str, description: str = ""):
        self.annotations[sequence] = (label, description)

    def rotate(self, bp: int, in_place: bool = False) -> None | Plasmid:
        rotate = lambda sequence: sequence[in_place:] + sequence[:in_place]

        if in_place:
            self.sequence = rotate(self.sequence)
        else:
            return Plasmid(rotate(self.sequence), self.annotations, self.linear)
