# %%
def prime_factors(number: int) -> list[int]:
    """
    Find and return the prime factors of a given number.

    Args:
        number (int): The number to find its prime factors.

    Returns:
        list[int]: A list containing the prime factors.

    Raises:
        ValueError: If the number is less than 2.
    ."""
    
    factors = []
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


print(prime_factors(56))

# %%



