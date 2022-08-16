from HackCurl.core.actions import ActionManagar

ACTIONS = ActionManagar.ACTIONS

DEFAULT_CONFIGS = {
    "mapping": {
        "normal": {
            "l": ACTIONS.GO_TO_NEXT_TAB,
            "j": ACTIONS.GO_TO_DOWN_PANEL,
            "gg": ACTIONS.OPEN_URL_FIELD,
            "<space><space>": ACTIONS.SUBMIT,
        }
    }
}
