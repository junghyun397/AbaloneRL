from abalone.HexDescription import HexDescription


_m1_size = 8
_m2_size = 8192

_indexed_vector = dict()


class HexVector:

    @staticmethod
    def get_indexed_vector(y: int, x: int, description: HexDescription):
        index_n_code = y * _m2_size + x * _m1_size + description.value

        if _indexed_vector[index_n_code] is None:
            _indexed_vector[index_n_code] = HexVector(y, x, description)

        return _indexed_vector[index_n_code]

    def __init__(self, y: int, x: int, description: HexDescription):
        self.y = y
        self.x = x
        self.description = description

    def copy(self) -> (int, int, HexDescription):
        HexVector(self.y, self.x, self.description)
