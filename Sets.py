#Un Set no és una estructura ordenada i no permet elements repetits

my_set = set()
my_other_set = {} #Inicialment serà un diccionari

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Jordi", "Caritg", 22}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("caritg40")
print(my_other_set) #No està ordenat

my_other_set.add("caritg40")
print(my_other_set) #No permet elements repetits

print("Jordi" in my_other_set)
print("Jordu" in my_other_set)

my_other_set.remove("Caritg")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set #Ens hem carregat el set (amb el "clear" el set segueix existint, amb el "del" NO)
# print(my_other_set)

my_set = {"Jordi", "Caritg", 22}
my_list = list(my_set) #No se sol fer, ja que es crea una llista amb un ordre aleatori
print(my_set)

my_other_set = "C++", "C#", "Python"
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_set)) #Recordem que no es permeten elements repetits

print(my_new_set.difference(my_set)) #Només escriu els que són diferents
