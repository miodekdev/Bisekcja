from typing import Callable


def _is_real(number: float) -> bool:
    return number not in {float("-inf"), float("inf"), float("nan")}

def find_zero(function: Callable[[float], float], domain: tuple[int, int], epsilon: float) -> float:
    assert all(_is_real(number) for number in (*domain, epsilon))
    assert epsilon > 0

    lower_bound, upper_bound = domain
    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound

    while abs(lower_bound - upper_bound) > epsilon:
        middle = (lower_bound+upper_bound) / 2
        if abs(function(middle)) < epsilon:
            return middle
        elif function(middle) * function(lower_bound) < 0:
            upper_bound = middle
        else:
            lower_bound = middle
    return float("nan")
