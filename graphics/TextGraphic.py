from abalone import FieldTemplate
from graphics.GraphicModule import GraphicModule


class TextGraphic(GraphicModule):

    def draw(self) -> None:
        print(FieldTemplate.get_text_board(self.base_vector))
        print("\n", "Turns:", self.base_vector[1], "Dropped black:", self.base_vector[3], "Dropped white", self.base_vector[4], "\n")
