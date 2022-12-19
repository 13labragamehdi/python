#boucle de type "tant que"
while False:
    print("ce message ne sera pas affiché")

#while True:
#    print("ce message sera affiché en boucle")

counter = 10

while counter:
    print(f"{counter = }")
    counter -= 1

for counter in range(0, 10):
    print(f"{counter = }")

fruits = ['abricot', 'baie', 'cerise']
#boucle de type for each == pour chaque
for foo in fruits:
    print(foo)

for counter in range(0, 10, 2):
    print(f'{counter = }')

for counter in range(10, 0, -1):
    print(f'{counter = }')

