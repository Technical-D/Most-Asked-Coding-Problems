def is_anagram(str1, str2):
    """
    Check if two strings are anagrams of each other.

    :param str1: str - First string
    :param str2: str - Second string
    :return: bool - True if anagrams, False otherwise
    """
    # Convert to lowercase for case insensitivity
    str1, str2 = str1.lower(), str2.lower()

    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Count frequency of each character
    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1  # Increment count

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1  # Decrement count

    return True

# Example Usage
if __name__ == "__main__":
    word1 = "Listen"
    word2 = "Silent"
    print(f"Are '{word1}' and '{word2}' anagrams? {is_anagram(word1, word2)}")  # Output: True
