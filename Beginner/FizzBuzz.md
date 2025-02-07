# FizzBuzz Problem

## Problem Statement
Write a function that prints numbers from `1` to `n` with the following conditions:
- If a number is divisible by `3`, print `"Fizz"`.
- If a number is divisible by `5`, print `"Buzz"`.
- If a number is divisible by both `3` and `5`, print `"FizzBuzz"`.
- Otherwise, print the number itself.

## Example
### Input:
n = 15
### Output:
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

## Constraints
- `1 <= n <= 10^4`

## Approach
1. Iterate through numbers from `1` to `n`.
2. Check divisibility:
   - If divisible by `3` and `5`, print `"FizzBuzz"`.
   - If divisible by `3`, print `"Fizz"`.
   - If divisible by `5`, print `"Buzz"`.
   - Otherwise, print the number.
3. **Time Complexity:** O(n) - Since we iterate through all numbers once.
