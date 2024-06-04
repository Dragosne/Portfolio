from coffee.coffee import Coffee

# clasa ce defineste tipul de cafea dorit pe baza clasei abstracte
class Espresso(Coffee):

    def __init__(self, intensitate=5, gramaj_lapte=0, gramaj_cafea=30, temperatura=90):
        super().__init__(intensitate, gramaj_lapte, gramaj_cafea, temperatura)

    def print_reteta_espresso(self):
        espresso = Espresso()
        print(f'intensity: {espresso.intensitate}')
        print(f'milk quantity: {espresso.gramaj_lapte}')
        print(f'coffee quantity: {espresso.gramaj_cafea}'),
        print(f'temperature: {espresso.temperatura}\n')

    def prepare(self):
        self.print_reteta_espresso()
        print('please wait espresso is preparing...\n')

    @classmethod
    def set_default_recipe(cls, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        super().set_default_recipe(intensitate=5, gramaj_lapte=0, gramaj_cafea=30, temperatura=90)
