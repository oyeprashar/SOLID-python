"""
In the good example, we've broken down the large interface into smaller, more specific ones. This allows for more flexibility in implementation.
"""


from abc import ABC, abstractmethod

# Bad example (violates ISP)
class MultiFunctionPrinter(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

# Good example (follows ISP)
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner, FaxMachine):
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass

class SimplePrinter(Printer):
    def print(self, document):
        pass
