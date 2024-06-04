from coffee.coffee import Coffee

# clasa ce defineste tipul de cafea dorit pe baza clasei abstracte
class Capucino(Coffee):

    def __init__(self, intensitate=5, gramaj_lapte=220, gramaj_cafea=30, temperatura=70):
        super().__init__(intensitate, gramaj_lapte, gramaj_cafea, temperatura)

    def print_reteta_capucino(self):
        capucino = Capucino()
        print(f'intensity: {capucino.intensitate}')
        print(f'milk quantity: {capucino.gramaj_lapte}')
        print(f'coffee quantity: {capucino.gramaj_cafea}'),
        print(f'temperature: {capucino.temperatura}\n')

    def prepare(self):
        self.print_reteta_capucino()
        print('please wait capucino is preparing...\n')

    @classmethod
    def set_default_recipe(cls, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        super().set_default_recipe(intensitate=5, gramaj_lapte=220, gramaj_cafea=30, temperatura=70)