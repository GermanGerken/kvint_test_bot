from transitions import Machine, State


class TelegramBot(object):

    states = ['asleep',
              'size_selected',
              'payment_selected',
              'flavour_selected']

    transitions = [
        {'trigger': 'asked_size', 'source': 'asleep', 'dest': 'size_selected', 'after': 'update_size'},
        {'trigger': 'asked_for_payment_method', 'source': 'size_selected', 'dest': 'payment_selected', 'after': 'update_payment'},
        {'trigger': 'asked_for_flavour', 'source': 'payment_selected', 'dest': 'flavour_selected','after': 'update_flavour'},
        {'trigger': 'confirmed', 'source': 'flavour_selected', 'dest': 'asleep'}, ]

    def __init__(self):
        self.size = ''
        self.pay_method = ''
        self.flavour = ''
        self.machine = Machine(model=self, states=TelegramBot.states, transitions=TelegramBot.transitions, initial='asleep')

    def update_size(self, msg):
        self.size = msg
        print(f'размер задан: {self.size}')


    def update_payment(self, msg):
        self.pay_method = msg
        print(f'способ оплаты задан: {self.pay_method}')


    def update_flavour(self, msg):
        self.flavour = msg
        print(f'Вкус пиццы задан: {self.flavour}')

