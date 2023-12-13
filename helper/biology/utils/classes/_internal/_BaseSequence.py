from __future__ import annotations
from typing import List, SupportsIndex, Any, Iterable


class _BaseSequence:
    unitType = None

    def __init__(self, sequence: List[unitType] = []) -> None:
        self.sequence = sequence

    def __add__(self, other: Iterable | unitType) -> None:
        # fix this @todo
        return self.__class__(
            [
                *self.sequence,
                *([c for c in other] if isinstance(other, Iterable) else [other]),
            ]
        )
    
    def __len__(self) -> int:
        return len(self.sequence)

    def __contains__(self, seq: str | _BaseSequence) -> bool:
        if isinstance(seq, str):
            return seq in self.sequence
        else:
            return seq.sequence in self.sequence

    def __getitem__(self, index: SupportsIndex) -> str:
        return self.sequence.__getitem__(index)

    def __len__(self) -> int:
        return self.sequence.__len__()

    def __str__(self) -> str:
        out = ""
        for c in self.sequence:
            out += str(c)
        return out
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"

    def count(self, seq: str) -> int:
        return str(self).count(seq)

    def find(self, seq) -> int:
        return str(self).find(seq)
