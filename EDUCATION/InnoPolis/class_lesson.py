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

    print(automat_1.can_run)
    print(automat_1.can_walk)

    automat_1.activate_bot()

    print(automat_1.can_run)
    print(automat_1.can_walk)

    automat_1.deactivate_bot()

    print(automat_1.can_run)
    print(automat_1.can_walk)
