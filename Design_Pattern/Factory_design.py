from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod 
    def person_method():
        """ Interface Method """

class student(IPerson):

    def __init__(self):
        self.name = "Basic student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1
    
if __name__ == "__main__":
    choice = input("what type of person do you want to create?\n")
    Person = PersonFactory.build_person(choice)
    Person.person_method()