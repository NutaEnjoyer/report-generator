from abc import ABC, abstractmethod


class BaseReport(ABC):
    def __init__(self, data: list[dict]):
        self.data = data
        self.report_json = self.generate_report()

    def __getattr__(self, name):
        if name == "json":
            return self.report_json
        
    @abstractmethod
    def __str__(self) -> str:
        pass
        
    @abstractmethod
    def generate_report(self) -> str:
        pass