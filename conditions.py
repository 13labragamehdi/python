import random

if True:
    print("La condition est vraie")
    print("Ce code est exécuté")

if False:
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")

conditions_vente = True

if conditions_vente == False :
    print("L'utilisateur a accepté les condtitions de vente")
else:
    print("L'utilisateur n'a pas accepté les condtitions de vente")

emails = random.randint(0, 3)
#elif c'est la meme chose que else if

if emails == 1:
    print("VOus avez un nouveau mail")
elif emails > 1:
    print(f"vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")

windows_closed = True
electricity_off = True

if windows_closed and electricity_off:
    print("Les fenetres sont fermees")
    print("L'electricité est coupée")
elif not windows_closed and electricity_off:
    print("Les fenetres ne sont pas fermees")
    print("L'elec est coupée")
elif windows_closed and not electricity_off:
    print("Les fenetres sont fermees")
    print("L'elec n'est pas coupée")
else:
    print('Les fenetres ne sont pas fermees')
    print("L'elec n'est pas coupée")

bank_card = True
cash = True

print(f"{bank_card =}")
print(f"{cash =}")


if bank_card or cash:
    print("On a un moyen de paiement")
else:
    print("On a aucun moyen de paiement")

ticket = True
vip = False
registration = False

if ticket or vip and registration