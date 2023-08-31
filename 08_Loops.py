# Los loops/bucles sirven para pasar por un mismo código varias veces

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #No es veu l'elif
    print("La meva condició és igual o més gran que 10")

print("La condició continua")

while my_condition < 20: #Es repetirà tants cops com compleixi la condició
    my_condition += 2
    if my_condition == 15:
        print("s'atura l'execusió")
        break
    print("La meva condició es menor que 20")

my_list = [3, 4, 10]

for element in my_list: #Es repetirà tants cops com elements tingui
    print(element)

my_set = {"Jordi", "Caritg", "Grimaldo", 22}

for element in my_set:
    print(element)

