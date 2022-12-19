class Carte:
    def __init__(self, couleur, symbole, rang):
        self._couleur = couleur
        self._symbole = symbole
        self._rang = rang

    def couleur(self):
        return self._couleur

    def symbole(self):
        return self._symbole

    def rang(self):
        return self._rang

    def nom(self):
        if self.rang() == 1:
            return 'as'
        elif self.rang() == 11:
            return 'valet'
        elif self.rang() == 12:
            return 'dame'
        elif self.rang() == 13:
            return 'roi'
        else:
            return str(self.rang())

    def plus_grand_que(self, carte):
        return self._rang > carte._rang

    def plus_petit_que(self, carte):
        return self._rang < carte._rang

    def egal_a(self, carte):
        return self._rang == carte._rang

    def __str__(self):
        return f"{self.nom()} de {self.symbole()}"

