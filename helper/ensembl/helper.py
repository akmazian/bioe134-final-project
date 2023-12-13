from typing import List, Iterable


def verifyEnsemblFormat(gene: str) -> bool:
    return len(gene) >= 4 and gene[0:3] == "ENS"


def removeVersionNumber(gene: str) -> str:
    """removes the version number in a gene in ensembl format"""
    if verifyEnsemblFormat(gene):
        return gene.split(".")[0]
    else:
        raise TypeError("use gene name in ensembl format")


def parseEnsemblIds(ids: Iterable) -> List[str]:
    return [removeVersionNumber(id) for id in ids]
