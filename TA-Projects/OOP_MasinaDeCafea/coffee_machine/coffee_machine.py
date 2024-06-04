from user.user import User
from coffee.capucino import Capucino
from coffee.espresso import Espresso
from coffee.americano import Americano
from coffee.cafe_latte import CafeLatte
from coffee_machine.meniuri import Meniuri
import time

# Clasa coffee machine contine actiunile de navigare in meniuri, si actiunile de cleaning, preparare etc
class CoffeeMachine:
    # variabile globale pentru selectarea user-ului si a retetei de cafea
    user = None
    coffee_type = None


    # metoda MENIU PRINCIPAL
    def main_menu_options(self):
        while True:
            try:
                main_menu = Meniuri()
                main_menu.print_main_menu()
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    self.select_user_profile()
                    break
                elif select_your_option == 2:
                    print('Clean operation Selected!')
                    time.sleep(2)
                    print('wait cleaning in progress ...')
                    time.sleep(6)
                    print()
                    self.start()
                    break
                elif select_your_option == 3:
                    print('\nThe Coffee Machine is shutting down.....\n')
                    time.sleep(5)
                    print('Run "main" to start again\n')
                    break
                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda selectare profil user sau vizitator
    def select_user_profile(self):
        global user
        while True:
            try:
                meniu_user_or_guest = Meniuri()
                meniu_user_or_guest.print_user_or_guest_menu()
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    self.select_registered_user()
                    break
                elif select_your_option == 2:
                    user = User("GUEST")
                    self.select_a_standard_coffee_receipe()
                    break
                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda selectare profil utilizator MOV, ROZ, FUCSIA
    def select_registered_user(self):
        global user
        while True:
            try:
                registered = Meniuri()
                registered.print_registered_user_menu()
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    print('\n>>> MOV user selected! <<<')
                    user = User("MOV")
                    self.select_coffee()
                    break
                elif select_your_option == 2:
                    print('\n>>> ROZ user selected! <<<')
                    user = User("ROZ")
                    self.select_coffee()
                    break
                elif select_your_option == 3:
                    print('\n>>> FUCSIA user selected! <<<')
                    user = User("FUCSIA")
                    self.select_coffee()
                    break
                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda selecteaza tip de cafea si printeaza reteta standard
    def select_coffee(self):
        global coffee_type
        standard_menu = Meniuri()
        standard_menu.print_standard_menu()
        while True:
            try:
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    # nu mai trebuie importata clasa, este importatat global, am lucrat meniul initial in alta clasa
                    # vreau totusi sa pastrez scrisa si aceasta abordare a.i. nu am sters liniile
                    from coffee.espresso import Espresso
                    coffee_type = 'Espresso'
                    option1 = Espresso()
                    print(f"\nThe standard recipe for Espresso is:")
                    print('---' * 15)
                    option1.print_reteta_espresso()
                    self.select_standard_or_personalised()
                    break
                elif select_your_option == 2:
                    from coffee.americano import Americano
                    coffee_type = 'Americano'
                    option2 = Americano()
                    print(f"\nThe standard recipe for Americano is:")
                    print('---' * 15)
                    option2.print_reteta_americano()
                    self.select_standard_or_personalised()
                    break
                elif select_your_option == 3:
                    from coffee.cafe_latte import CafeLatte
                    coffee_type = 'CafeLatte'
                    option3 = CafeLatte()
                    print(f"\nThe standard recipe for Cafe Latte is:")
                    print('---' * 15)
                    option3.print_reteta_cafe_latte()
                    self.select_standard_or_personalised()
                    break
                elif select_your_option == 4:
                    from coffee.capucino import Capucino
                    coffee_type = 'Capucino'
                    option4 = Capucino()
                    print(f"\nThe standard recipe for Capucino is:")
                    print('---' * 15)
                    option4.print_reteta_capucino()
                    self.select_standard_or_personalised()
                    break

                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda selecteaza preferinta reteta standard sau personalizata
    # utilizata pentru utilizator inregistrat
    def select_standard_or_personalised(self):
        global coffee_type
        while True:
            try:
                standard_or_personalised = Meniuri()
                standard_or_personalised.print_standard_or_personalised()
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    if coffee_type == 'CafeLatte':
                        prepare = CafeLatte()
                        prepare.prepare()
                    elif coffee_type == 'Espresso':
                        prepare = Espresso()
                        prepare.prepare()
                    elif coffee_type == 'Capucino':
                        prepare = Capucino()
                        prepare.prepare()
                    elif coffee_type == 'Americano':
                        prepare = Americano()
                        prepare.prepare()
                    time.sleep(5)
                    print('YOUR COFFEE IS READY\n')
                    self.start()
                    break
                elif select_your_option == 2:
                    self.personalised_coffee_recipe()
                    break
                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda reteta de cafea standard
    def select_a_standard_coffee_receipe(self):
        global user
        while True:
            try:
                standard_menu = Meniuri()
                standard_menu.print_standard_menu()
                select_your_option = int(input('Type the option number: '))
                if select_your_option == 1:
                    espresso = Espresso()
                    user.choose_coffee(espresso)
                    espresso.prepare()
                    time.sleep(5)
                    print('YOUR COFFEE IS READY\n')
                    self.start()
                    break
                elif select_your_option == 2:
                    americano = Americano()
                    user.choose_coffee(americano)
                    americano.prepare()
                    time.sleep(5)
                    print('YOUR COFFEE IS READY\n')
                    self.start()
                    break
                elif select_your_option == 3:
                    cafe_latte = CafeLatte()
                    user.choose_coffee(cafe_latte)
                    cafe_latte.prepare()
                    time.sleep(5)
                    print('YOUR COFFEE IS READY\n')
                    self.start()
                    break
                elif select_your_option == 4:
                    capucino = Capucino()
                    user.choose_coffee(capucino)
                    capucino.prepare()
                    time.sleep(5)
                    print('YOUR COFFEE IS READY\n')
                    self.start()
                    break
                else:
                    print('ERROR: Please type a valid number!\n')
            except ValueError:
                print('ERROR: Please type a number!\n')


    # metoda pentru introducerea ingredientelor pentru reteta
    # personalizata in cazul utilizatorilor inregistrati
    def personalised_coffee_recipe(self):
        global user
        personalised = Meniuri()
        personalised.print_personalised_menu()
        while True:
            try:
                intensitate = int(input('Type the intensity (1 - 5): '))
                if 1 <= intensitate <= 5:
                    print("OK")
                    break
                else:
                    print('ERROR: Type a valid intensity')
            except ValueError:
                print('ERROR: Type a valid number')
        while True:
            try:
                gramaj_lapte = int(input('Type the milk quantity (0 - 250 ml): '))
                if 0 <= gramaj_lapte <= 250:
                    print("OK")
                    break
                else:
                    print('ERROR: Type a valid milk quantity')
            except ValueError:
                print('ERROR: Type a valid number')
        while True:
            try:
                gramaj_cafea = int(input('Type the coffee quantity (10 - 100 g): '))
                if 10 <= gramaj_cafea <= 100:
                    print("OK")
                    break
                else:
                    print('ERROR: Type a valid coffee quantity')
            except ValueError:
                print('ERROR: Type a valid number')
        while True:
            try:
                temperatura = int(input('Type the temperature (60 - 95 ^C): '))
                if 60 <= temperatura <= 95:
                    print("OK")
                    break
                else:
                    print('ERROR: Type a valid temperature')
            except ValueError:
                print('ERROR: Type a valid number')
        # am folosit o alta abordare pentru printarea retetei personalizate
        # valori introduse de utilizatori de la tastatura
        print('YOUR SELECTION IS:\n',
              f'intensity: {intensitate}\n',
              f'milk quantity: {gramaj_lapte}\n',
              f'coffee quantity: {gramaj_cafea}\n',
              f'temperature: {temperatura}\n'
              )
        user.personalised_coffee()
        time.sleep(5)
        print('YOUR COFFEE IS READY\n')
        self.start()


    # metoda start aparat de cafea
    def start(self):
        print('==' * 10)
        print('"THE COFFEE MACHINE"')
        print('==' * 10)
        print('Press enter to start...')
        start_the_machine = input()
        self.main_menu_options()