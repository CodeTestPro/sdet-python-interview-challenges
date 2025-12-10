"""
Challenge: Change a string such that first character is upper case,
second is lower case and so on.

Example: 'Hello' -> 'HeLlO'
"""

def alternating_case(text):
    """
    Converts string to alternating case pattern.
    
    Args:
        text: Input string
        
    Returns:
        String with alternating case pattern
    """
    if not text:
        return text
    
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)


if __name__ == '__main__':
    test_cases = [
        'Hello',
        'JavaProgramming',
        'interview',
        'SdEt'
    ]
    
    for test in test_cases:
        print(f'Input: {test} -> Output: {alternating_case(test)}')
