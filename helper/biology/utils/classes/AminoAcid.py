from ._internal._BaseUnit import _BaseUnit


class AminoAcid(_BaseUnit):
    Phenylalanine = None
    Leucine = None
    Isoleucine = None
    Methionine = None
    Valine = None
    Serine = None
    Proline = None
    Threonine = None
    Alanine = None
    Tyrosine = None
    STOP = None
    Histidine = None
    Glutamine = None
    Asparagine = None
    Lysine = None
    AsparticAcid = None
    GlutamicAcid = None
    Cysteine = None
    Tryptophan = None
    Arginine = None
    Glycine = None

    def __init__(self, abbr1, abbr3, name) -> None:
        self.abbr1 = abbr1
        self.abbr3 = abbr3
        self.name = name
        
    def __str__(self):
        return self.abbr1

    @classmethod
    def initialize(cls):
        cls.Phenylalanine = cls("F", "Phe", "Phenylalanine")
        cls.Leucine = cls("L", "Leu", "Leucine")
        cls.Isoleucine = cls("I", "Ile", "Isoleucine")
        cls.Methionine = cls("M", "Met", "Methionine")
        cls.Valine = cls("V", "Val", "Valine")
        cls.Serine = cls("S", "Ser", "Serine")
        cls.Proline = cls("P", "Pro", "Proline")
        cls.Threonine = cls("T", "Thr", "Threonine")
        cls.Alanine = cls("A", "Ala", "Alanine")
        cls.Tyrosine = cls("Y", "Tyr", "Tyrosine")
        cls.STOP = cls("*", "***", "STOP")
        cls.Histidine = cls("H", "His", "Histidine")
        cls.Glutamine = cls("Q", "Gln", "Glutamine")
        cls.Asparagine = cls("N", "Asn", "Asparagine")
        cls.Lysine = cls("K", "Lys", "Lysine")
        cls.AsparticAcid = cls("D", "Asp", "Aspartic Acid")
        cls.GlutamicAcid = cls("E", "Glu", "Glutamic Acid")
        cls.Cysteine = cls("C", "Cys", "Cysteine")
        cls.Tryptophan = cls("W", "Trp", "Tryptophan")
        cls.Arginine = cls("R", "Arg", "Arginine")
        cls.Glycine = cls("G", "Gly", "Glycine")
