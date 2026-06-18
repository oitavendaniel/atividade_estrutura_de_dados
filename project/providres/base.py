from abc import ABC, abstractmethod

class DatabaseProvider(ABC):
    
    @abstractmethod
    def get_all(self, table: str):
        pass

    @abstractmethod
    def create(self, table: str, data: dict):
        pass