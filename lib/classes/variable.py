class Variable:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return f"Variable({self.name})"

    def __repr__(self):
        return self.__str__()
