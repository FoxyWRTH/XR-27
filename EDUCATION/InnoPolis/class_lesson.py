"""
Немного ООП.
"""


class Unit773():
    """Kill Bot"""

    def __init__(self, model, serial_number, name):
        self.can_run = False
        self.can_walk = False
        self.model = model
        self.serial_number = serial_number
        self.name = name

    def activate_bot(self, can_walk=True, can_run=True):
        """Activate Kill Bot"""
        self.can_walk = can_walk
        self.can_run = can_run

    def deactivate_bot(self, can_walk=False, can_run=False):
        """Deactivate Kill Bot"""
        self.can_walk = can_walk
        self.can_run = can_run


class Unit774(Unit773):
    """Another Kill Bot"""

    def __init__(self, model, serial_number, name):
        super().__init__(model, serial_number, name)
        self.can_fly = True
        self.can_shot = True


if __name__ == '__main__':
    automat_1 = Unit773('U773', 'U773_0101', 'Little Killer')
    automat_2 = Unit774('U774', 'U774_0102', 'Sub Killer')

    print('\nInitialize automat - 1')
    print(f'Automat - 1, can you walk? - {automat_1.can_walk}\n'
          f'Automat - 1, can you run? - {automat_1.can_run}')

    print('\nOk, press "F" to activating... ')
    automat_1.activate_bot()

    print(f'Automat - 1, can you walk? - {automat_1.can_walk}\n'
          f'Automat - 1, can you run? - {automat_1.can_run}')

    print('\nOk, press "D" to deactivating... ')
    automat_1.deactivate_bot()

    print(f'Automat - 1, can you walk? - {automat_1.can_walk}\n'
          f'Automat - 1, can you run? - {automat_1.can_run}')

    print('\nInitialize automat - 2')
    print(f'Automat - 2, can you walk? - {automat_2.can_walk}\n'
          f'Automat - 2, can you run? - {automat_2.can_run}')

    print('\nOk, press "F" to activating... ')
    automat_2.activate_bot()

    print(f'Automat - 2, can you walk? - {automat_2.can_walk}\n'
          f'Automat - 2, can you run? - {automat_2.can_run}')

    print('\nOk, press "D" to deactivating... ')
    automat_2.deactivate_bot()

    print(f'Automat - 2, can you walk? - {automat_2.can_walk}\n'
          f'Automat - 2, can you run? - {automat_2.can_run}')
