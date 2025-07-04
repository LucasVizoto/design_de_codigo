from abc import ABC, abstractmethod


class Company_Bad_exemple: 
    def do_work(self, worker: int) -> None:
        if worker == 1:
            print('Programmer creating code')
        elif worker == 2:
            print('Seller selling the product')
        elif worker == 3:
            print('Human Resources hiring new devs')
        elif worker == 4:
            print('Frontend raising bugs for production')
        else:
            print('Error, no worker')
# no exemplo acima, se eu precisar criar algo novo, ele vai 
# ir crescendo indefinidamente

class MyInterface(ABC):
    @abstractmethod
    def make():
        ...

class Company_correct:
    def do_work(self, worker: MyInterface) -> None:
        worker.make()

class Programmer(MyInterface):
    def make(): print('Programmer creating code')

class Seller(MyInterface):
    def make(): print('Seller selling the product')

class RH(MyInterface):
    def make(): print('Human Resources hiring new devs')

programmer = Programmer()
seller = Seller()
rh = RH()

company = Company_correct()
company.do_work(programmer)
company.do_work(seller)
company.do_work(rh) 