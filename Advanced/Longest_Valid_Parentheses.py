def longest_valid_parentheses(s):
    """
    Given a string containing just the characters '(' and ')', find the length of the longest
    valid (well-formed) parentheses substring.

    :param s: str - Input string of parentheses
    :return: int - Length of the longest valid parentheses substring
    """
    stack = [-1]  # Initialize stack with -1 as a base index
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push index of '(' onto the stack
        else:
            stack.pop()  # Pop last '(' index

            if stack:
                max_length = max(max_length, i - stack[-1])  # Calculate length
            else:
                stack.append(i)  # Push current index as base for next valid substring

    return max_length

# Example Usage
if __name__ == "__main__":
    s = "(()))())("
    print(longest_valid_parentheses(s))  # Output: 4
