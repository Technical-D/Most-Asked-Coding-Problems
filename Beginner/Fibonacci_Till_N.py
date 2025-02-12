def fibonacci_till_n(n):
    """
    Generate Fibonacci series up to n using list indexing.

    :param n: int - The limit up to which Fibonacci numbers are generated.
    :return: list - Fibonacci sequence up to n.
    """
    if n < 0:
        return []

    fib_series = [0, 1]  # Initialize Fibonacci list

    while True:
        next_term = fib_series[-1] + fib_series[-2]  # Using list indexing
        if next_term > n:
            break
        fib_series.append(next_term)

    return fib_series

# Example Usage
if __name__ == "__main__":
    limit = 50
    print(f"Fibonacci Series up to {limit}: {fibonacci_till_n(limit)}")
