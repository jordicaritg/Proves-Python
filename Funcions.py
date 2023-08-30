# Funcions: Intentaran resoldre un problema concret, i amb un mímin d'errors

def my_function ():
    print("Això és una funció")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5,7)
sum_two_values(58489,78431)
sum_two_values("5","7")
sum_two_values(4.3,5)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value #return és per guardar-me el resultat en una variable

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Caritg", name = "Jordi")