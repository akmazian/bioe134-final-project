from typing import Tuple, Literal
from ..utils import RestrictionEnzyme, Plasmid, revcomp


class GibsonAssembly:
    def __init__(
        self,
        backbone: str | Plasmid,
        cutting_site: str | RestrictionEnzyme,
    ) -> None:
        self.sequence = backbone
        self.cutting_site = cutting_site

    def __call__(
        self,
        insert: str,
        reverse_insert: bool = False,
        binding_length: int = 20,
        overhang_length: int = 20,
        preserve_cutting_site: Literal["none", "both", "5 prime", "3 prime"] = "none",
    ) -> Tuple[str, str]:
        """
        @param preserve_cutting_site = 'none' | 'both' | '5 prime' | '3 prime'. If cutting_site is defined to be a string, then only 'none' and 'both' are valid options
        @return a pair of forward and reverse primer to use to amplify the insert
        """

        # param type assertions
        if isinstance(self.cutting_site, str) and preserve_cutting_site in [
            "5 prime",
            "3 prime",
        ]:
            raise TypeError(
                'preserve_cutting_site has an illegal value. only use "none" or "both" when cutting_site is defined as a string'
            )

        if preserve_cutting_site not in ["none", "both", "5 prime", "3 prime"]:
            raise TypeError(
                'preserve_cutting_site has an illegal value, only use "none" | "both" | "5 prime" | "3 prime"'
            )

        if len(insert) < binding_length * 2:
            raise TypeError(
                "binding_length has an illegal value. the resulting primers will have overlaps. reduce binding_length or increase insert length"
            )

        # param validations (not enforced, only warnings)
        if binding_length < 15 or binding_length > 30:
            print(
                "binding_length is possibly too short or too long, which might lead to insufficient PCR. Use around 15 to 30 for optimal result"
            )

        if overhang_length < 15 or overhang_length > 30:
            print(
                "overhang_length is possibly too short or too long, which might lead to insufficient Gibson Assembly. Use around 15 to 30 for optimal result"
            )

        if reverse_insert:
            insert = insert[::-1]

        sequence = (
            self.sequence if isinstance(self.sequence, str) else self.sequence.sequence
        )

        insertion_index = (
            sequence.find(self.cutting_site)
            if isinstance(self.cutting_site, str)
            else sequence.find(self.cutting_site.recognition_site)
            + self.cutting_site.cutting_index
        )

        if insertion_index < overhang_length:
            sequence += sequence
            insertion_index += len(sequence)

        # fix preserve cutting site logic
        forward_primer = str(
            sequence[insertion_index - overhang_length : insertion_index]
            + insert[0:binding_length]
        ).upper()
        reverse_primer = revcomp(
            insert[len(insert) - binding_length : -1]
            + sequence[insertion_index : insertion_index + overhang_length]
        ).upper()

        # print message if there are multiple binding sites

        return forward_primer, reverse_primer
