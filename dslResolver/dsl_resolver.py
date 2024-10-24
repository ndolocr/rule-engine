from abc import ABC, abstractmethod

class DSLResolver(ABC):
    @abstractmethod
    def get_resolver_keyword(self) -> str:
        """Return the keyword that this resolver handles."""
        pass

    @abstractmethod
    def resolve_value(self, keyword: str) -> object:
        """Return the resolved value for the keyword."""
        pass
