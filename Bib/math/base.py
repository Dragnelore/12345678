from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def __init__(self,a):
        pass
    
    @abstractmethod
    def execute(self,*args):
        pass

    @property
    def pochet(self):
        return "HVOST VMETSO NOG"
    #пасхалка
    