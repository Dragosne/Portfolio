from coffee.coffee import Coffee

# clasa ce defineste tipul de cafea dorit pe baza clasei abstracte
class Americano(Coffee):

    def __init__(self, intensitate=3, gramaj_lapte=0, gramaj_cafea=50, temperatura=70):
        super().__init__(intensitate, gramaj_lapte, gramaj_cafea, temperatura)

    def print_reteta_americano(self):
        americano = Americano()
        print(f'intensity: {americano.intensitate}')
        print(f'milk quantity: {americano.gramaj_lapte}')
        print(f'coffee quantity: {americano.gramaj_cafea}'),
        print(f'temperature: {americano.temperatura}\n')

    def prepare(self):
        self.print_reteta_americano()
        print('please wait americano is preparing...\n')

    @classmethod
    def set_default_recipe(cls, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        super().set_default_recipe(intensitate=3, gramaj_lapte=0, gramaj_cafea=50, temperatura=70)
