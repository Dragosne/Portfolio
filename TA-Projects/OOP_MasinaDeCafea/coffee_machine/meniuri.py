
# clasa Meniuri contine metodele de print a meniurilor aparatului de cafea
class Meniuri:

    def print_main_menu(self):
        print('MAIN MENU')
        print('---' * 10)
        print('1. Prepare a coffee')
        print('2. Clean the coffee machine')
        print('3. Exit')
        print('---' * 10)

    def print_user_or_guest_menu(self):
        print("\n")
        print('REGISTERED USER OR GUEST?')
        print('---' * 10)
        print('1. REGISTERED USER')
        print('2. GUEST')
        print('---' * 10)

    def print_registered_user_menu(self):
        print("\n")
        print('SELECT USER PROFILE')
        print('---' * 10)
        print('1. MOV profile')
        print('2. ROZ profile')
        print('3. FUCSIA profile')
        print('---' * 10)

    def print_standard_menu(self):
        print("\n")
        print('SELECT A COFFEE')
        print('---' * 10)
        print('1. Espresso')
        print('2. Americano')
        print('3. Cafe Latte')
        print('4. Capucino')
        print('---' * 10)

    def print_standard_or_personalised(self):
        print("\n")
        print('SELECT A RECIPE')
        print('---' * 10)
        print('1. Standard recipe')
        print('2. Personalised recipe')
        print('---' * 10)

    def print_personalised_menu(self):
        print("\n")
        print('INSERT YOUR CHOICES')
        print('---' * 10, "\n")

    def choosing_coffee_to_personalise_menu(self):
        print("\nWhich coffee you want to customize?".upper())
        print('---' * 10)
        print('1. Espresso')
        print('2. Americano')
        print('3. Cafe Latte')
        print('4. Capucino')
        print('---' * 10)
