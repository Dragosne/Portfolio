from coffee.coffee import Coffee

# clasa ce defineste tipul de cafea dorit pe baza clasei abstracte
class CafeLatte(Coffee):

    def __init__(self, intensitate=3, gramaj_lapte=150, gramaj_cafea=50, temperatura=80):
        super().__init__(intensitate, gramaj_lapte, gramaj_cafea, temperatura)

    def print_reteta_cafe_latte(self):
        cafe_latte = CafeLatte()
        print(f'intensity: {cafe_latte.intensitate}')
        print(f'milk quantity: {cafe_latte.gramaj_lapte}')
        print(f'coffee quantity: {cafe_latte.gramaj_cafea}'),
        print(f'temperature: {cafe_latte.temperatura}\n')

    def prepare(self):
        self.print_reteta_cafe_latte()
        print('please wait cafe_latte is preparing...\n')

    @classmethod
    def set_default_recipe(cls, intensitate, gramaj_lapte, gramaj_cafea, temperatura):
        super().set_default_recipe(intensitate=3, gramaj_lapte=150, gramaj_cafea=50, temperatura=80)