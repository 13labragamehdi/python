my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)

my_number1 = 123
# interpolation avec une f-string
my_text3 = f"Nombre = {my_number1}"
print(my_text3)
my_text4 = f"""
Le nombre
est
{my_number1}
foo
"""
print(my_text4)

#afficher des accolades dans une heredoc f-string
my_text5 = f"""
{{
foo
}}
{{bar}}
"""
print(my_text5)

my_number2 = 3.14
my_text6 = "Le nombre PI est " +  str(my_number2) + "\nEt le nombre"
print(my_text6)

# tronquer un float dans une interpolation
my_number3 = 1 / 3
my_text7 = f"1 / 3 ~= {my_number3:.4f}"
print(my_text7)

# les interpolations acceptent les expressions
my_text8 = f"1 + 1 = {1 + 1}"
print(my_text8)

# l'ecriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à qqun 

    name str ce paramètre indique le nom de la personne  à saluer
    return None"""
    print(f"Salut {name}")

#appel d'une fonction
hello('Toto')
#affiche la doc d'une fonction
help(hello)

my_text9 = "Lorem Ipsum, dolor sit amet consecutor adipassion"
#longueur d'une str
my_number4 = len(my_text9)
print(my_number4)

#trouve la poistion d'une str dans une autre str
my_number5 = my_text9.find('dolor')
my_number5 = my_text9.find('dolor', my_number5 + 1)

print(my_number5)

#compte le nombre d'occurence d'une str dans une autre str
my_number6 = my_text9.count('Lorem')
print(my_number6)
#remplacement non permanant
print(my_text9.replace('Lorem', 'Foo'))
#remplacement permanant
my_text9 = my_text9.replace("Lorem", "Foo")
print(my_text9)
#eclate une str en liste utilisant l'espace comme caractere de separation
my_list1 = my_text9.split()
print(my_list1)
#la fonction len() peut aussi etre utilisée avec des listes pour compter le nombore d'elements
print(len(my_list1))