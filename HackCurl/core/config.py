from HackCurl.core.actions import ActionManagar
from HackCurl.core.file_buffer import FileBuffer

ACTIONS = ActionManagar.ACTIONS

DEFAULT_CONFIGS = {
    "mapping": {
        # Moving
        "h": ACTIONS.GO_TO_LEFT_PANEL,
        "j": ACTIONS.GO_TO_DOWN_PANEL,
        "k": ACTIONS.GO_TO_UP_PANEL,
        "l": ACTIONS.GO_TO_RIGHT_PANEL,
        "gg": ACTIONS.OPEN_URL_FIELD,
        "<CR>": ACTIONS.SUBMIT,
        "e": ACTIONS.EDIT,
        "a": ACTIONS.ADD,
        "i": ACTIONS.INSERT,
    }
}


# TODO: Make it Singleton
class Config:
    _config_file: FileBuffer

    def load_file(self, filePath: str):
        pass

    def getMapping(self):
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
