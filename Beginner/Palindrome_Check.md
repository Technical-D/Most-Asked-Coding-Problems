# Palindrome Check

## Problem Statement
Write a function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same forward and backward, ignoring case and non-alphanumeric characters.

## Example

### Input:
```plaintext
racecar
```
### Output:
```plaintext
True
```

### Input:
```plaintext
hello
```
### Output:
```plaintext
False
```

## Constraints
- The input string consists only of printable ASCII characters.
- The function should ignore spaces, punctuation, and case sensitivity.

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the input string.
- **Space Complexity**: O(n), due to storing the cleaned version of the string.
