class Node:
    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
