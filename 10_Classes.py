# Classes: Ens serveix per dotar de principi i fi a una classe

class MyPerson: #Les classes sí que porten majúscula i sense barra baixa
    pass

print(MyPerson)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"
    
    def walk (self):
        print(f"{self.full_name} Està caminant")

my_person = Person("Jordi", "Caritg")
print(my_person.name)
print(my_person.full_name)

my_person.walk()

