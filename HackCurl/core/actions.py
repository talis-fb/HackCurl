class Actions:
    # TODO: Aqui (ou na classe de ActionsManager) serao importados as classes de interface regras de negocios. É aqui que serao chamados
    #   os eventos e chamadas solicitadas pelo usuario. NOTA: Aqui nao deverá ter regras de negocios ou implementação hard-code
    #   aqui é o caminho entre o input do usuario (o disparo de uma acao) e as funções das outras classes. Sendo assim, essas funções
    #   apenas devem chamar APIs com abstrações de outras classes
    def OPEN_BODY_FIELD(self):
        pass

    def OPEN_BODY_FIELD_WITH_TEXT_EDITOR(self):
        pass

    def OPEN_HEADERS_FIELD(self):
        pass

    def OPEN_HEADERS_FIELD_WITH_TEXT_EDITOR(self):
        pass

    def OPEN_URL_FIELD(self):
        pass

    def GO_TO_RIGHT_PANEL(self):
        pass

    def GO_TO_LEFT_PANEL(self):
        pass

    def GO_TO_UP_PANEL(self):
        pass

    def GO_TO_DOWN_PANEL(self):
        pass

    def GO_TO_NEXT_TAB(self):
        pass

    def GO_TO_PREVIOUS_TAB(self):
        pass

    def SUBMIT(self):
        pass

    def SELECT_METHOD(self):
        pass


class ActionManagar:
    ACTIONS = Actions()
