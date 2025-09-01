def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    
    total = 0
    
    for l in range(n):
        for r in range(l, n):
            # Get unique values in subarray A[l:r+1]
            unique_vals = set(a[l:r+1])
            
            if not unique_vals:
                continue
                
            # Sort the unique values
            sorted_vals = sorted(unique_vals)
            
            # Count number of maximal contiguous ranges
            # Each gap creates a new range
            operations = 1
            for i in range(1, len(sorted_vals)):
                if sorted_vals[i] != sorted_vals[i-1] + 1:
                    operations += 1
            
            total += operations
    
    return str(total)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": """4
1 3 1 4""",
            "expected": "16"
        },
        {
            "input": """5
3 1 4 2 4""",
            "expected": "23"
        },
        {
            "input": """10
5 1 10 9 2 5 6 9 1 6""",
            "expected": "129"
        }
    ]
    
    print("Running test cases...")
    for i, test_case in enumerate(test_cases, 1):
        result = candidate_func(test_case["input"])
        expected = test_case["expected"]
        
        print(f"\nTest case {i}:")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Match: {result == expected}")
        
        if result != expected:
            print("❌ FAILED")
            break
        else:
            print("✅ PASSED")
    else:
        print("\n🎉 All test cases passed!") 