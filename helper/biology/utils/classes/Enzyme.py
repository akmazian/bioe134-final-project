from ._internal._BaseUnit import _BaseUnit


class Enzyme(_BaseUnit):
    Category: str
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.__str__()
