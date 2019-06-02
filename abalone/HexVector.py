from abalone.HexDescription import HexDescription


m1_size = 8
m2_size = 8192

indexed_vector = dict()


class HexVector:

    @staticmethod
    def get_indexed_vector(y: int, x: int, description: HexDescription):
        index_n_code = y * m2_size + x * m1_size + description.value

        if indexed_vector[index_n_code] is None:
            indexed_vector[index_n_code] = HexVector(y, x, description)

        return indexed_vector[index_n_code]

    def __init__(self, y: int, x: int, description: HexDescription):
        self.y = y
        self.x = x
        self.description = description

    def copy(self) -> (int, int, HexDescription):
        HexVector(self.y, self.x, self.description)
