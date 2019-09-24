from abalone import FieldTemplate
from graphics.GraphicModule import GraphicModule


class TextGraphic(GraphicModule):

    def _init_ui_components(self) -> None:
        pass

    def _draw(self) -> None:
        print(FieldTemplate.get_text_board(self._base_vector))
        print(">> Turns: {0}, Dropped black: {1}, Dropped white: {2}\n"
              .format(self._base_vector[1], self._base_vector[3], self._base_vector[4]))
