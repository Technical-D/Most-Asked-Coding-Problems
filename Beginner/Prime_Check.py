def is_prime(n):
    """
    Check if a number is prime.

    :param n: int - The number to check.
    :return: bool - True if prime, False otherwise.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):  # Checking divisibility up to sqrt(n)
        if n % i == 0:
            return False

    return True

# Example Usage
if __name__ == "__main__":
    number = 29
    print(f"Is {number} a prime number? {is_prime(number)}")  # Output: True
