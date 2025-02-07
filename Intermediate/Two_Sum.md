# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

## Example
### Input:
nums = [2, 7, 11, 15] 
target = 9
### Output:
[0, 1]

Explanation: `nums[0] + nums[1] = 2 + 7 = 9`.

## Constraints
- Each input has **exactly one solution**.
- The same element cannot be used twice.
- You may return the answer in **any order**.
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Approach
### 1️⃣ Brute Force (O(n²))
- Use a nested loop to check every pair of numbers.
- **Drawback:** Slow for large arrays.

### 2️⃣ Optimized Approach (O(n))
- Use a **hash map (dictionary)** to store numbers and their indices.
- Iterate once and check if `target - current_number` exists in the dictionary.
- If found, return the indices; otherwise, store the number in the dictionary.

**Time Complexity:** `O(n)`, since we traverse the list once.