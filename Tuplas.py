# tupla és un conjunt de valors, però que són immutables

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.79, "Jordi", "Caritg")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple.index("Jordi"))
print(my_tuple.count("Jordi"))
print(my_tuple + my_other_tuple)

#Si vull modificar una tupla (no aconsellable), puc transformar-la a llista, o borra-la (amb del)
