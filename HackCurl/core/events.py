from abc import ABC, abstractmethod


class EventListerner(ABC):
    @abstractmethod
    def update(self, data=None):
        pass


class EventManagar:
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
        list_observers = self._listeners.get(event)

        if not list_observers:
            return

        self._last_event = event
        for observer in list_observers:
            observer.update(data)
