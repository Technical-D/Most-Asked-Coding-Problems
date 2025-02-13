# Anagram Checker

## Problem Statement
Given two strings, determine if they are **anagrams** of each other.  
An anagram is when two words have the same letters in different order.

## Example
### Input:
str1 = "Listen" str2 = "Silent"

### Output:
True

Explanation: Both words contain the same letters.

### Input:
str1 = "Hello" str2 = "World"

### Output:
False

## Constraints
- Case **does not** matter (`"Listen" == "Silent"`).
- Only **letters** are considered (no spaces, punctuation).

## Approach
1. Convert both strings to **lowercase**.
2. If **lengths are different**, return `False` immediately.
3. Use a **dictionary (hashmap)** to count character occurrences in `str1`.
4. Iterate through `str2` and **decrement** counts.
   - If a character is missing or count becomes negative, return `False`.
5. **Time Complexity:** `O(n)`, **Space Complexity:** `O(1)` (fixed size dictionary).