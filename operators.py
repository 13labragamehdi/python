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