from abc import ABC, abstractmethod


class EventListerner(ABC):
    @abstractmethod
    def update(self, data=None):
        pass


class EventManeger:
    _last_event: str | None = None

    _listeners: dict[str, list[EventListerner]] = {
        "SUBMIT": [],
        "BODY_EDIT": [],
        "METHOD_EDIT": [],
        "HEADERS_EDIT": [],
        "AUTHENTICATION_EDIT": [],
        "RESPONSE": [],
        "RESPONSE_STATUSCODE_202": [],
        "RESPONSE_STATUSCODE_404": [],
        "REQUEST_CANCELED": [],
        "ERROR": [],
    }

    EVENTS = list(_listeners.keys())

    def addEventListener(self, event: str, observer: EventListerner) -> None:
        self._listeners[event].append(observer)
        pass

    def removeEventListener(self, event: str, observer: EventListerner) -> None:
        self._listeners[event].remove(observer)
        pass

    def notify(self, event: str, data=None) -> None:
        list_listeners = self._listeners.get(event)

        if not list_listeners:
            return

        self._last_event = event
        for observer in list_listeners:
            observer.update(data)
