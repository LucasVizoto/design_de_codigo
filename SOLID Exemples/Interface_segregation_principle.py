from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def load(self): ...
    def view(self): ...
    def format(self): ...
    def calculate(self): ...

class PDF(Document):
    def load(self): 
        print('loading pdf')
    def calculating(self): 
        print('loading pdf')

#------------------------------------------

#certo seria 

class DocumentTXT:
    @abstractmethod
    def load(self): ...
    def format(self): ...

class DocumentPDF:
    @abstractmethod
    def load(self): ...
    def view(self): ...