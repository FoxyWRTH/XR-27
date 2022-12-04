"""
Немного ООП.
"""


class Unit773():
    def __init__(self, model, serial_number, name):
        self.model = model
        self.serial_number = serial_number
        self.name = name


class Unit774(Unit773):
    def __init__(self, model, serial_number, name):
        super().__init__(model, serial_number, name)


if __name__ == '__main__':
    automat_1 = Unit773('U773', 'U773_0101', 'Little Killer')
    automat_01 = Unit774('U774', 'U774_0102', 'Sub Killer')

    print(f'You see some automat... Let se...\n'
          f'{automat_1.model}... '
          f'{automat_1.name}...'
          f'{automat_1.serial_number}')

    print(f'\nYou see some another automat... Let se...\n'
          f'{automat_01.model}... '
          f'{automat_01.name}...'
          f'{automat_01.serial_number}')
