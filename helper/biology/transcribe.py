def transcribe(seq: str) -> str:
    """transcribes a protein coding sequence into mRNA, does not handle splicing and other modifications"""
    return seq.upper().replace("T", "U")


def reverseTranscribe(seq: str) -> str:
    """reverse transcribe an mRNA into it's protein coding DNA sequence"""
    return seq.upper().replace("U", "T")
