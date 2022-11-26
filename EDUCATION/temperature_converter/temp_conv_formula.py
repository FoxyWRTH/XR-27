"""
Набор формул.
"""


def celsius_in_fahrenheit(cel):
    """Цельсии в Фаренгейты"""
    cel_far = cel * 1.8 + 32
    return cel_far


def celsius_in_kelvin(cel):
    """Цельсии в Кельвины"""
    cel_kel = cel + 273
    return cel_kel


def fahrenheit_in_celsius(far):
    """Фаренгейты в цельсии"""
    far_cel = (far - 32) / 1.8
    return far_cel


def fahrenheit_in_kelvin(far):
    """Фаренгейты в Кельвины"""
    far_kel = (far + 459) / 1.8
    return far_kel


def kelvin_in_celsius(kel):
    """Кельвины в Цельсии"""
    kel_cel = kel - 273
    return kel_cel


def kelvin_in_fahrenheit(kel):
    """Кельвины в Фаренгейты"""
    kel_far = kel * 1.8 - 459
    return kel_far
