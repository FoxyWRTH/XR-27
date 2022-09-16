import random

lists_of_things = [1, 2, 3, 4, 5]


def random_element(some_list):
    try:
        result = random.choice(some_list)
        return result
    except IndexError:
        return None

