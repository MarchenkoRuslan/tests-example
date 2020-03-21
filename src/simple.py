import math


def check_simple(num):
    if num == 0:
        return False
    for divider in range(2, math.floor(num**0.5) + 1):
        if not (num % divider):
            return False
    return True
