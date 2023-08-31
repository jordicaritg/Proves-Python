# Llista: Conjunt de valors

mylist = list()
my_other_list = [3, 4]
mylist = ["Jordi", "Sergi", "Mama", "Papa"]
print(len(mylist))
print(type(mylist))
print(mylist[3])
print(mylist.count("Sergi"))
nom_fill_1 = mylist[0]
print(nom_fill_1)
print(mylist + my_other_list)
mylist.insert(3, 2)
print(mylist)
mylist.remove(2)
print(mylist)
mylist_eliminant_Jordi = mylist.pop(1)
print(mylist_eliminant_Jordi)
mylist[0] = "Jordu"
print(mylist)
mylist = ["Jordi", "Sergi", "Mama", "Papa"]
mylist[0] = "Jordu"
print(mylist)
print(mylist[1:2])
print(mylist[1:3])

print("hola que ase")

