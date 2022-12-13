fruits = ["ananas", "banane", "cerise"]
print(fruits)

#acces en lecture au 0eme element de la liste
print(fruits[0])

my_fruit = fruits[0]
print(my_fruit)
# acces en ecriture au 0eme element de la liste
fruits[0] = "abricot"
print(fruits)
print(fruits[0])

index = 0
print(fruits[index])
index += 1
print(fruits[index])
index += 1
print(fruits[index])

my_count = len(fruits)

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])
    