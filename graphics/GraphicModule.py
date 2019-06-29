from abalone import AbaloneModel


class GraphicModule:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls):
        cls._instance = cls()
        cls.instance = cls._get_instance
        return cls._instance

    def __init__(self):
        self.update_frequency = 60

        self.abalone_model = None
        self.alive_ui = False
        self.active_playable = False

    # Basic Setting

    def set_model(self, abalone_model: AbaloneModel.AbaloneAgent) -> None:
        self.abalone_model = abalone_model
        self._update_state()

    def run_ui(self) -> None:
        self.alive_ui = True

    def kill_ui(self) -> None:
        self.alive_ui = False

    def set_playable(self, value: bool) -> None:
        self.active_playable = value

    # Main

    def _main_loop(self) -> None:
        while self.alive_ui:
            if self.active_playable:
                pass

    def _update_state(self) -> None:
        pass

    # Graphic

    def _draw_abalone_board(self) -> None:
        pass

    def _draw_abalone_field(self) -> None:
        pass

    def _draw_abalone_state(self) -> None:
        pass
