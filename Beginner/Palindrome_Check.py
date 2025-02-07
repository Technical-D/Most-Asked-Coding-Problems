def is_palindrome(s):
    # Convert string to lowercase
    s = s.lower()
    
    # Filter out non-alphanumeric characters
    filtered_chars = []
    for char in s:
        if char.isalnum():
            filtered_chars.append(char)
    
    # Use a stack to store first half of the string
    stack = []
    n = len(filtered_chars)
    mid = n // 2

    # Push first half onto stack
    for i in range(mid):
        stack.append(filtered_chars[i])

    # If length is odd, skip the middle character
    start = mid if n % 2 == 0 else mid + 1

    # Compare second half with stack elements
    for i in range(start, n):
        if stack.pop() != filtered_chars[i]:
            return False

    return True

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("No lemon, no melon"))  # True
