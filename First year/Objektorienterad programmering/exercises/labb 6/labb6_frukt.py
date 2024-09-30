class Frukt:
    def __init__(self, namn, antalFrukt, pris):
        self.__namn = namn
        self.__antal = antalFrukt
        self.__pris = pris

    def set_namn(self, namn):
        self.__namn = namn

    def set_antal(self, antalFrukt):
        self.__antal = antalFrukt

    def set_pris(self, pris):
        self.__pris = pris

    def get_namn(self):
        return self.__namn

    def get_antal(self):
        return self.__antal

    def get_pris(self):
        return self.__pris

    def __str__(self):
         return 'Frukt: '+ self.get_namn()+ \
                '\nAntal: '+ str(self.get_antal())+ \
                '\nPris: '+ str(self.get_pris())
         


