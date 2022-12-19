import random
import math
# = affectation
foo = 123
# + addition
foo = 123 + 42
foo = foo + 42
foo += 42 #(veut dire la meme chose que la ligne du dessus)
# / division
foo = 123 / 42
# // division entière
foo = 123 // 42
# * multiplication
foo = 50 * 40
# - soustraction
foo = 123 - 42
foo = foo - 42
foo -= 42 #( veut dire la meme chose que la ligne du dessus)
# ** puissance ( pour python sinon ^)
foo = 2 ** 2
foo = 2 ** 3
foo = foo ** 2
foo = 2 ** foo
# sqrt() racine carré
foo = math.sqrt(4)
foo = 4 ** 0.5
# racine cubique
foo = 4 ** (1/3)
# % modulo ( reste de la division )
foo = 4 % 3
foo = random.randint(1,100)
print(foo % 2)

# les operateurs de comparaison

# l'égalité ==
result = 1 == 1
print(result)

# les grandeurs
result = 123 < 42
print(result)
result = 123 <= 42
result = 123 > 42
result = 123 >= 42

# inégalité
result = 123 != 42
print(result)

# Encadrement
# < > <= >=
my_number = random.randint(0,100)
print(my_number)
result = 0 <= my_number < 50
print(result)
result = 50 < my_number <= 100
print(result)

# operateur " and "
result = True and False # False
print(result)
result = False and True # False
print(result)
result = True and True # True
print(result)
result = False and False # False
print(result)



# operateur " or ""
result = True or False # True
print(result)
result = False or True # True
print(result)
result = True or True # True
print(result)
result = False or False # False
print(result)

# operateur not ( negation)

result = not True
print(result)
result = not False
print(result)

#on peut utiliser d'autres type de données que l'ont converti  en booléen avec les opérateurs boléens
a = random.randint(0, 1)
b = random.randint(0, 1)
result = bool(a) and bool(b)
print(a, b)
print(result)

# utlisation un peu spéciale des comparaisons de grandeur

result = "abc">"bcd"

fruits = ['abricot', 'baie', 'cerise']
result = 'ananas' in fruits
print(result)
result = 'cerise' in fruits
print(result)
