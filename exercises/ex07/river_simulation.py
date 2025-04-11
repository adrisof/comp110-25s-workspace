from river import River
from bear import Bear
from fish import Fish

my_river = River(num_fish=10, num_bears=2)

my_river.fish = [Fish() for _ in range(10)]
my_river.bears = [Bear() for _ in range(2)]

my_river.view_river()
