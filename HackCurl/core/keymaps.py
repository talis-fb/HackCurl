from HackCurl.core.config import Config
from HackCurl.core.actions import FileBuffer

ACTIONS = ActionManagar.ACTIONS


class Keymap:
    _c = Config()

    def run(self, key: str):
        action = self._c.getMapping()[key]
        action()
        pass
