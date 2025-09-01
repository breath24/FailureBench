def candidate_func(input_str):
    S = input_str.strip()
    n = len(S)
    
    # Get the reverse of S
    rev_S = S[::-1]
    
    # Find the longest suffix of S that matches a prefix of reverse(S)
    for i in range(n):
        # Check if S[i:] (suffix of S) equals rev_S[:n-i] (prefix of reverse(S))
        if S[i:] == rev_S[:n-i]:
            # We found the longest matching suffix/prefix
            # Append the remaining part of reverse(S) to S
            return S + rev_S[n-i:]
    
    # If no match found (shouldn't happen), append entire reverse except last char
    return S + rev_S[:-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "ABC",
            "expected": "ABCBA"
        },
        {
            "input": "Z", 
            "expected": "Z"
        },
        {
            "input": "TREE",
            "expected": "TREERT"
        }
    ]
    
    print("Running test cases...")
    for i, test_case in enumerate(test_cases, 1):
        result = candidate_func(test_case["input"])
        expected = test_case["expected"]
        
        # Check if result is a palindrome and has correct prefix
        is_palindrome = result == result[::-1]
        has_correct_prefix = result.startswith(test_case["input"])
        
        print(f"\nTest case {i}:")
        print(f"Input: {test_case['input']}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Is palindrome: {is_palindrome}")
        print(f"Has correct prefix: {has_correct_prefix}")
        print(f"Match: {result == expected}")
        
        if result != expected:
            print("❌ FAILED")
            break
        else:
            print("✅ PASSED")
    else:
        print("\n🎉 All test cases passed!") 