
# clasa utilizator
class User:

    def __init__(self, user_profile):
        self.user_profile = user_profile

    def choose_coffee(self, coffee):
        print(f'\n{self.user_profile} profile and {coffee.__class__.__name__} coffee were selected.\n')
    # coffee.prepare()

    def personalised_coffee(self):
        print(f'\nCongrats {self.user_profile} profile! you discovered a new coffee recipe.\n')
        print('please wait until your special coffee is ready ......\n')