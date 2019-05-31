from abalone.HexDescription import HexDescription


class HexVector:

    indexed_vector = None

    @staticmethod
    def get_indexed_vector(y: int, x: int, description: HexDescription):
        pass

    def __init__(self, y: int, x: int, description: HexDescription):
        self.y = y
        self.x = x
        self.description = description

    def copy(self) -> (int, int, HexDescription):
        HexVector(self.y, self.x, self.description)
