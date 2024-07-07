import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    """
    Generate set of random number for lottery tickets

    Returns:
        List of lottery numbers
    """
    try:
        if min < 1 or max > 1000 or quantity > max or quantity < min:
            return []
    except TypeError:
        print("Input parameters are not integers")
        return []
    else:
        list = random.sample(range(min, max + 1), quantity)
        list.sort()
        return list
