import abc


class ICmd(abc.ABC):
    name = None
    description = None
    action = None

    @abc.abstractmethod
    def __name__(self) -> str:
        pass

    @abc.abstractmethod
    def __description__(self) -> str:
        pass

    @abc.abstractmethod
    def __action__(self, ctx):
        pass
