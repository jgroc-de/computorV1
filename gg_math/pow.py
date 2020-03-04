def pow(number: float, power: int) -> float:
    result = number
    for _ in range(1, power):
        result *= number

    return result
