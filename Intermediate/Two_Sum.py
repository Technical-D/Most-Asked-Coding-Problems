def two_sum(nums, target):
    """
    Given an array of integers `nums` and an integer `target`, 
    return the indices of the two numbers that add up to `target`.

    :param nums: List[int] - List of integers
    :param target: int - Target sum
    :return: List[int] - Indices of the two numbers
    """
    num_dict = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num  # Find the required complement

        if complement in num_dict:
            return [num_dict[complement], i]  # Return indices of two numbers

        num_dict[num] = i  # Store the current number with its index

    return []  # Return empty list if no solution is found

# Example Usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]
