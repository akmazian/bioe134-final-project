from .Enzyme import Enzyme


class RestrictionEnzyme(Enzyme):
    Category = "Restriction Enzyme"

    def __init__(
        self,
        name: str,
        recognition_site: str,
        cutting_index: int,
        complement_cutting_index: int | None = None,
    ) -> None:
        """
        @param cutting_index - cutting site on top strand, counting from 5' end
        @param complement_cutting_index - cutting site on bottom strand, also counting from 5' end. Leave blank for blunt restrictions
        """
        self.enzyme_name = name
        self.recognition_site = recognition_site
        self.cutting_index = cutting_index
        self.complement_cutting_index = (
            len(recognition_site) - complement_cutting_index
            if complement_cutting_index
            else len(recognition_site) - cutting_index
        )
        self.blunt = not complement_cutting_index

    def __str__(self) -> str:
        return f"{self.enzyme_name} Restriction Enzyme: recognizes {self.recognition_site} and produces a {'sticky' if not self.blunt else 'blunt'} end."
