from abc import ABC, abstractmethod

class DSLResolver(ABC):
    @abstractmethod
    def get_resolver_keyword(self) -> str:
        pass

    @abstractmethod
    def resolve_value(self, keyword: str) -> object:
        pass
