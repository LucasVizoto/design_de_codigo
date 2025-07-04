from abc import ABC, abstractmethod

class NotificatorInterface(ABC):
    @abstractmethod
    def send_notification(): ...
    
####### Em outro aquivo

class NotificatorEmail(NotificatorInterface):
    def send_notification(self, message: str):
        print(f'Sending Email: {message}')

####### Em outro aquivo

class NotificatorSMS(NotificatorInterface):
    def send_notification(self, message: str):
        print(f'Sending Email: {message}')

####### Em outro aquivo
# from .notificator_email import NotificatorEmail

class ClientService:
    def __init__(self, notificator:NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str)->None:
        self.notificator.send_notification(message)
    