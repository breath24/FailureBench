from collections import Counter

def findValidPair(s):
    """
    Find the first valid pair of adjacent digits where:
    - The digits are different
    - Each digit appears exactly as many times as its numeric value
    
    Args:
        s: String consisting only of digits
    
    Returns:
        String representing the first valid pair, or empty string if none exists
    """
    # Count frequency of each digit
    count = Counter(s)
    
    # Check each adjacent pair from left to right
    for i in range(len(s) - 1):
        first_digit = s[i]
        second_digit = s[i + 1]
        
        # Check if digits are different
        if first_digit != second_digit:
            # Check if each digit appears exactly as many times as its value
            if count[first_digit] == int(first_digit) and count[second_digit] == int(second_digit):
                return first_digit + second_digit
    
    return ""


# Test with provided examples
if __name__ == "__main__":
    # Example 1
    s1 = "2523533"
    result1 = findValidPair(s1)
    print(f"Example 1: s = \"{s1}\"")
    print(f"Result: \"{result1}\"")
    print(f"Expected: \"23\"")
    print()
    
    # Example 2
    s2 = "221"
    result2 = findValidPair(s2)
    print(f"Example 2: s = \"{s2}\"")
    print(f"Result: \"{result2}\"")
    print(f"Expected: \"21\"")
    print()
    
    # Example 3
    s3 = "22"
    result3 = findValidPair(s3)
    print(f"Example 3: s = \"{s3}\"")
    print(f"Result: \"{result3}\"")
    print(f"Expected: \"\"")
    print()
    


