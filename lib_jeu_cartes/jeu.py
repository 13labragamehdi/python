class Jeu:
    def __init__(self, ordre_cartes=None):
        if ordre_cartes != None:
            self._ordre_cartes = ordre_cartes
        else:
            self.regle_classique()

    def regle_classique(self):
        self._ordre_cartes = [i for i in range(0, 14)]

    def regle_as_au_top(self):
        self._ordre_cartes = [0, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def regle_deux_au_top(self):
        self._ordre_cartes = [0, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def plus_grand_que(self, carte1, carte2):
        return self._ordre_cartes[carte1.rang()] > self._ordre_cartes[carte2.rang()]

    def plus_petit_que(self, carte1, carte2):
        return self._ordre_cartes[carte1.rang()] < self._ordre_cartes[carte2.rang()]

    def egal_a(self, carte1, carte2):
        return self._ordre_cartes[carte1.rang()] == self._ordre_cartes[carte2.rang()]

