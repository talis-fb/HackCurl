from HackCurl.core.actions import Actions
from HackCurl.core.file_buffer import FileBuffer
from HackCurl.utils.singleton import SingletonClass

ACTIONS = Actions()

DEFAULT_CONFIGS = {
    "mapping": {
        # Moving
        "h": ACTIONS.GO_TO_LEFT_PANEL,
        "j": ACTIONS.GO_TO_DOWN_PANEL,
        "k": ACTIONS.GO_TO_UP_PANEL,
        "l": ACTIONS.GO_TO_RIGHT_PANEL,
        "gg": ACTIONS.OPEN_URL_FIELD,
        # Editing
        "e": ACTIONS.EDIT,
        "a": ACTIONS.ADD,
        "i": ACTIONS.INSERT,
        # Submit
        "<CR>": ACTIONS.SUBMIT,
    }
}


# TODO: Make it Singleton
class Config(SingletonClass):
    _config_file: FileBuffer

    def load_file(self, filePath: str):
        pass

    def getMapping(self):
        # Aqui, se ele leu algum arquivo em load_files, entao retorna ele, senao, as padrões
        return DEFAULT_CONFIGS["mapping"]


#
# {
#
#     default:
#         maps: normal
#             i: GO_TO_RIGHT
#             l: GO_TO_RIGHT
#             fat: GO_TO_RIGHT
#             g: .
#                 a: FOI
#             gb:
# }
#
