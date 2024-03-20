from abc import ABCMeta, abstractclassmethod

from Factory_design_method import Person

class IPerson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        print("I am s student")
        """" Interface Method """


class ProxyPerson(IPerson):

    def person_method(self):
        print("I am a person")

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()
    
    def person_method(self):
        print("I am proxy functionality!")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
