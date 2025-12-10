CHALLENGE_CHECKLIST.md"""
Challenge: Check if a string is a palindrome
Example: 'racecar' is a palindrome, 'hello' is not
"""

def is_palindrome(text):
    """Check if text is a palindrome (ignoring spaces and case)"""
    clean = text.lower().replace(' ', '')
    return clean == clean[::-1]

if __name__ == '__main__':
    tests = ['racecar', 'A man a plan a canal Panama', 'hello', 'level']
    for test in tests:
        print(f'"{test}" is palindrome: {is_palindrome(test)}')
