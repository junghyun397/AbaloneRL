class AbaloneRole:

    def __init__(self, max_turns: int = 1000,
                 movable_stones: int = 3,
                 end_dropped_stone: int = 6):
        self.max_turns = max_turns
        self.movable_stones = movable_stones
        self.end_dropped_stone = end_dropped_stone
