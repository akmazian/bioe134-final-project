from typing import List
from ._internal._BaseSequence import _BaseSequence



class Sequence(_BaseSequence):
    unitType = str
    
    def __init__(self, sequence: List[str] | str = []) -> None:
        self.sequence = (
            sequence
            if isinstance(sequence, list)
            else [c for c in sequence]
            if isinstance(sequence, str)
            else sequence.sequence
        )

    def findAllCDS(self):
        sequence = str(self)
        windows = [sequence, sequence[1:], sequence[2:]]

        import re

        cdss = []

        for window in windows:
            cdss.extend(re.findall(r"(ATG(?:[ATCG]{3})+?TAA|TAG|TGA)", window))

        return [cds for cds in cdss if len(cds) > 10]
