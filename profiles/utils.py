import random


available_numbers: list = [x for x in range(10)]
size: int = 26


def generate_konto_nummer():
    new_number_list: list = [str(random.choice(available_numbers)) for _ in range(size)]
    new_number_str: str = "".join(new_number_list)
    return new_number_str
