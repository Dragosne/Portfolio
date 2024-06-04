from abc import ABC, abstractmethod
# clasa abstracta pentru tipurile de cafea, defineste variabilele si metodele obligatorii
class Coffee(ABC):

    # constructor
    def __init__(self, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        self.intensitate = intensitate
        self.gramaj_lapte = gramaj_lapte
        self.gramaj_cafea = gramaj_cafea
        self.temperatura = temperatura

    # metoda preparare cafea
    @abstractmethod
    def prepare(self):
        pass

    # metoda de setare a retetei standard
    @abstractmethod
    def set_default_recipe(cls, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        cls.default_recipe = (intensitate, gramaj_lapte, gramaj_cafea, temperatura)