# Diccionaris: Estructura per emmagatzemar dades amb relació clau-valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nom":"Jordi", "Cognom":"Caritg", "Edat":22, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nom":"Jordi",
    "Edat":22,
    "Llenguate":{"Python","C#","Arduino"}
}

print(my_dict)
print(len(my_dict))
print(my_dict["Nom"])

my_dict["Nom"] = "Jordu"
print(my_dict)

my_dict["Carrer"] = "Toledo"
print(my_dict)

del my_dict["Carrer"]
print(my_dict)

print("Jordu" in my_dict) #falç perquè busca per claus, no valors
print("Nom" in my_dict) #ara sí

print(my_dict.items()) #Llistat
print(my_dict.values()) #Llistat només valors
print(my_dict.keys()) #Llistat només claus

my_new_dict = my_dict.fromkeys("Nom") #Ens treu els valors
print(my_new_dict)

my_list = ["Nom", "Pis", 1]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

print(tuple(my_new_dict))
print(list(my_new_dict.values()))
print(set(my_new_dict))
