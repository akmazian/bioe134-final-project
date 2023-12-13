from typing import List, Dict
from .Peptide import Peptide


class Protein:
    def __init__(
        self, peptides: List[Peptide], annotations: Dict[str, str] = {}
    ) -> None:
        self.peptides = peptides
        self.annotations = annotations

    def __contains__(self, peptide: Peptide) -> bool:
        return peptide in self.peptides
