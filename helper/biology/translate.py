from .transcribe import reverseTranscribe
from .utils import AminoAcid as AA, Peptide
from typing import Dict


def translate(seq: str, truncate: bool = False) -> str:
    """
    translate a sequence into protein
    :param truncate: specifies whether the translation should be truncated after an in-frame stop codon
    """
    codon_table: Dict[str, AA] = {
        "ATA": AA.Isoleucine,
        "ATC": AA.Isoleucine,
        "ATT": AA.Isoleucine,
        "ATG": AA.Methionine,
        "ACA": AA.Threonine,
        "ACC": AA.Threonine,
        "ACG": AA.Threonine,
        "ACT": AA.Threonine,
        "AAC": AA.Asparagine,
        "AAT": AA.Asparagine,
        "AAA": AA.Lysine,
        "AAG": AA.Lysine,
        "AGC": AA.Serine,
        "AGT": AA.Serine,
        "AGA": AA.Arginine,
        "AGG": AA.Arginine,
        "CTA": AA.Leucine,
        "CTC": AA.Leucine,
        "CTG": AA.Leucine,
        "CTT": AA.Leucine,
        "CCA": AA.Proline,
        "CCC": AA.Proline,
        "CCG": AA.Proline,
        "CCT": AA.Proline,
        "CAC": AA.Histidine,
        "CAT": AA.Histidine,
        "CAA": AA.Glutamine,
        "CAG": AA.Glutamine,
        "CGA": AA.Arginine,
        "CGC": AA.Arginine,
        "CGG": AA.Arginine,
        "CGT": AA.Arginine,
        "GTA": AA.Valine,
        "GTC": AA.Valine,
        "GTG": AA.Valine,
        "GTT": AA.Valine,
        "GCA": AA.Alanine,
        "GCC": AA.Alanine,
        "GCG": AA.Alanine,
        "GCT": AA.Alanine,
        "GAC": AA.AsparticAcid,
        "GAT": AA.AsparticAcid,
        "GAA": AA.GlutamicAcid,
        "GAG": AA.GlutamicAcid,
        "GGA": AA.Glycine,
        "GGC": AA.Glycine,
        "GGG": AA.Glycine,
        "GGT": AA.Glycine,
        "TCA": AA.Serine,
        "TCC": AA.Serine,
        "TCG": AA.Serine,
        "TCT": AA.Serine,
        "TTC": AA.Phenylalanine,
        "TTT": AA.Phenylalanine,
        "TTA": AA.Leucine,
        "TTG": AA.Leucine,
        "TAC": AA.Tyrosine,
        "TAT": AA.Tyrosine,
        "TAA": AA.STOP,
        "TAG": AA.STOP,
        "TGC": AA.Cysteine,
        "TGT": AA.Cysteine,
        "TGA": AA.STOP,
        "TGG": AA.Tryptophan,
    }

    protein = Peptide()

    # to keep formating consistent
    seq = reverseTranscribe(seq)

    for i in range(0, len(seq) // 3 * 3, 3):
        codon = seq[i : i + 3]
        aa: AA = codon_table[codon]
        protein += aa
        if truncate and aa.abbr1 == "*":
            break

    return protein
