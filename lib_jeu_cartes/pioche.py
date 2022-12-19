from .carte import Carte
import random

class Pioche:
    def __init__(self, cartes=None):
        if cartes == None:
            cartes = []

        self._cartes = cartes

    def init_deck(self):
        self._cartes.clear()

        for i in range(0, 4):
            if i % 2 == 0:
                couleur = 'rouge'
            else:
                couleur = 'noir'

            if i == 0:
                symbole = 'cœur'
            elif i == 1:
                symbole = 'pique'
            elif i == 2:
                symbole = 'carreau'
            else:
                symbole = 'treffle'

            for j in range(1, 14):
                carte = Carte(couleur, symbole, j)
                self._cartes.append(carte)

    def distribuer(self, n):
        cartes = []

        for i in range(0, n):
            carte = self._cartes.pop()
            cartes.append(carte)

        return cartes

    def choisir_au_hasard(self, n):
        cartes = []

        for i in range(0, n):
            carte = random.choice(self._cartes)
            cartes.append(carte)
            self._cartes.remove(carte)

        return cartes

    def remettre(self, cartes):
        self._cartes.extend(cartes)
        cartes.clear()

    def __str__(self):
        return ', '.join([str(carte) for carte in self._cartes])

