"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        surviving_bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = surviving_fish
        self.bears = surviving_bears

    def bears_eating(self) -> None:
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self) -> None:
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self) -> None:
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend([Fish() for _ in range(new_fish)])

    def repopulate_bears(self) -> None:
        new_bears = len(self.bears) // 2
        self.bears.extend([Bear() for _ in range(new_bears)])

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def remove_fish(self, amount: int) -> None:
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)  #

    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


def one_river_week(self) -> None:
    for _ in range(7):
        self.one_river_day()
