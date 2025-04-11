"""File to define Fish class."""


class Fish:
    def __init__(self) -> None:
        self.age = 0

    def one_day(self) -> None:
        self.age += 1
