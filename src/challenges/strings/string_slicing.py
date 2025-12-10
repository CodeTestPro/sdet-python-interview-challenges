"""
Challenge: String Slicing - Extract substrings using Python slicing
Example: 'Hello World'[0:5] = 'Hello', 'Hello World'[::-1] = 'dlroW olleH'
"""

def string_slicing():
    """Demonstrates various string slicing operations"""
    s = "Python Programming"
    
    # First 6 characters
    first_six = s[:6]
    
    # Last 6 characters
    last_six = s[-6:]
    
    # Every 2nd character
    every_second = s[::2]
    
    # Reverse string
    reversed_str = s[::-1]
    
    return first_six, last_six, every_second, reversed_str


if __name__ == '__main__':
    first, last, every2, rev = string_slicing()
    print(f'First 6: {first}')
    print(f'Last 6: {last}')
    print(f'Every 2nd char: {every2}')
    print(f'Reversed: {rev}')
