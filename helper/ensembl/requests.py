from typing import Iterable, Literal


def BasePostRequest(
    extension: str,
    data: str | dict,
    headers={"Content-Type": "application/json"},
    assembly: Literal["grch37", "grch38"] = "grch38",
) -> object:
    import json

    import requests

    return requests.post(
        f"https://{'grch37.' if assembly == 'grch37' else ''}rest.ensembl.org/{extension}",
        headers=headers,
        data=data if isinstance(data, str) else json.dumps(data),
    ).json()


def LookUpRequest(
    ids: Iterable, assembly: Literal["grch37", "grch38"] = "grch38"
) -> dict:
    base = {}
    for i in range(0, len(ids), 1000):
        print(f"LookUpRequest: iter #{i}")
        base.update(
            BasePostRequest(
                "lookup/id", data={"ids": list(ids[i : i + 1000])}, assembly=assembly
            )
        )
    return base


def SequenceRequest(
    ids: Iterable, assembly: Literal["grch37", "grch38"] = "grch38"
) -> dict:
    base = []
    for i in range(0, len(ids), 50):
        print(f"SequenceRequest: iter #{i}")
        base += BasePostRequest(
            "sequence/id", data={"ids": list(ids[i : i + 50])}, assembly=assembly
        )
    return {seq: seq for seq in base}
