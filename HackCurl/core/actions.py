from HackCurl.core.events import EventManeger
from HackCurl.utils.singleton import SingletonClass


class Actions(SingletonClass):
    # TODO: Aqui (ou na classe de ActionsManager) serao importados as classes de interface regras de negocios. É aqui que serao chamados
    #   os eventos e chamadas solicitadas pelo usuario. NOTA: Aqui nao deverá ter regras de negocios ou implementação hard-code
    #   aqui é o caminho entre o input do usuario (o disparo de uma acao) e as funções das outras classes. Sendo assim, essas funções
    #   apenas devem chamar APIs com abstrações de outras classes

    events = EventManeger()

    def exec(self, name: str, optional_data=None):
        action = getattr(Actions, name)
        action(optional_data)

    def OPEN_BODY_FIELD(self):
        pass

    def ADD(self):
        pass

    def INSERT(self):
        pass

    def EDIT(self):
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
        self.events.notify("SUBMIT")

    def SELECT_METHOD(self):
        pass


#
#
# class ActionManagar:
#     ACTIONS = Actions()
#     def aa(self):
#         cc = self.ACTIONS.__getattribute__("SUBMIT")
#         print(cc)
#         print(cc)
#         pass
