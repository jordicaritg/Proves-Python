#Condicionals

my_condition = True

if my_condition:         #És el mateix que if my_conditon == True
    print("S'executa la condició if")

print("L'execució continua")

my_other_condition = 5 * 2

if my_other_condition == 11:         
    print("S'executa la condició if")

print("L'execució continua")

if my_other_condition >= 20 and my_other_condition <= 10:      
    print("S'executa la condició del if <= 10")
else:
    print("S'executa l'else")

print("L'execució continua")

if my_other_condition >= 20 and my_other_condition <= 10:      
    print("S'executa la condició del if <= 10")
elif my_condition == 11: #si l'if no es compleix però això si, s'executara això
    print("aquí veiem el elif")
else: #això en última instància
    print("S'executa l'else del elif")

print("L'execució continua")

if not my_other_condition == 9:
    print("jejejejej")