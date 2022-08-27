from HackCurl.utils.singleton import SingletonClass
from HackCurl.core.config import Config


class Keymap(SingletonClass):
    _maps = Config().getMapping()

    def run(self, key: str):
        action = self._maps[key]
        action()
        pass
