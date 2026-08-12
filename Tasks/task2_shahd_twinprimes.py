def twin_primes(n: int) -> None:
    """
    Print all twin prime pairs less than n.

    Two prime numbers are called twin primes if their difference is 2.

    Args:
        n (int): The upper limit for finding twin primes.

    Returns:
        None
    """

    def is_prime(num: int) -> bool:
        """Check whether a number is prime."""
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    for i in range(2, n - 2):
        if is_prime(i) and is_prime(i + 2):
            print(f"{i} and {i + 2}")

if __name__ == "__main__":
    print("Testing twin_primes:")
    twin_primes(20)
    print("Testing twin_primes:")
    twin_primes(1000)
