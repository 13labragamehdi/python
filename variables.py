# l'opérateur d'affectation = permet d'injecter une valeur dans une variable

# integer, nombre entier

my_number1 = 123
my_number2 = -42
my_number6 = 0

print(my_number1)
print(my_number2)
print(type(my_number1))

 # float, nombre à virgule flotante

my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0

print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number5))

# bool, booléen 

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None, valeur nulle
# null, nil

my_none = None
print(my_none)
print(type(my_none))

# string, chaîne de caractères
# double quote ou simple quote, c'est pareil ( pour python )

my_text1 = "Ceci est une chaîne de caractères"
my_text2 = "Ceci est aussi une chaîne de caracères"

print(my_text1)
print(my_text2)

# \caractère d'échappement
# \n saut de ligne

my_text3 = "abc\neojfeojf\nekfjf"
my_text4 = "\\"
my_text5 = "John \"Foo\" Doe"
print(my_text3)
print(my_text4)
print(my_text5)
print(type(my_text1))

my_text6 = """abc
def
ghi"""
print(my_text6)
print(type(my_text6))

# permutation de la valeur des variables

a = 123
b = 42
a, b = b, a
print(a, b) 


a = 123
b = 42

c = a
a = b
b = c
print(a, b)

# variante qui marche qu'avec des nombres
a = 123
b = 42
c = a + b 
a = c - a 
b = c - b 
print(a, b)