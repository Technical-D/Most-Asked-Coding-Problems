def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    :param n: int - Non-negative integer
    :return: int - Factorial of n
    """
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 and 1 is 1
    return n * factorial(n - 1)  # Recursive call

# Example Usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")  # Output: 120
