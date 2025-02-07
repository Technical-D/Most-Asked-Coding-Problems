def fizz_buzz(n):
    """
    Prints numbers from 1 to n with the following conditions:
    - Print "Fizz" for multiples of 3
    - Print "Buzz" for multiples of 5
    - Print "FizzBuzz" for multiples of both 3 and 5
    - Otherwise, print the number itself
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example Usage
fizz_buzz(20)
