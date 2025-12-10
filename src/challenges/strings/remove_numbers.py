"""
Challenge: String s = 'sub53od73th'; Eliminate the numbers alone. Print the Alphabets.

Example: 'sub53od73th' -> 'subodth'
"""

def remove_numbers(text):
    """
    Removes all numeric digits from the string.
    
    Args:
        text: Input string with mixed characters and numbers
        
    Returns:
        String with only alphabetic characters
    """
    return ''.join(char for char in text if not char.isdigit())


if __name__ == '__main__':
    test_cases = [
        'sub53od73th',
        'abc123def456ghi',
        'java2024programming'
    ]
    
    for test in test_cases:
        print(f'Input: {test} -> Output: {remove_numbers(test)}')
