def longest_unique_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    :param s: str - Input string
    :return: int - Length of the longest unique substring
    """
    char_index = {}  # Dictionary to store the last index of characters
    max_length = 0
    left = 0  # Left pointer of the sliding window

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move the left pointer to avoid duplicates
        
        char_index[char] = right  # Update the last index of the character
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

# Example Usage
if __name__ == "__main__":
    s = "abcabcbb"
    print(longest_unique_substring(s))  # Output: 3 ("abc")
