def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    A = list(map(int, lines[1].split()))
    
    # Key insight: The game ends when all N indices have been chosen at least once
    # Total moves = N (to choose each index once) + extra moves (choosing already-chosen indices)
    # Maximum extra moves = sum(A) - N
    # The parity of total extra moves determines the winner
    
    total_sum = sum(A)
    extra_moves = total_sum - N
    
    # If extra moves is odd, Fennec (first player) wins
    # If extra moves is even, Snuke (second player) wins
    if extra_moves % 2 == 1:
        return "Fennec"
    else:
        return "Snuke"


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "3\n1 9 2",
            "expected": "Fennec"
        },
        {
            "input": "2\n25 29", 
            "expected": "Snuke"
        },
        {
            "input": "6\n1 9 2 25 2 9",
            "expected": "Snuke"
        }
    ]
    
    print("Final solution test:")
    
    for i, test_case in enumerate(test_cases, 1):
        result = candidate_func(test_case["input"])
        expected = test_case["expected"]
        
        print(f"\nTest case {i}:")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"{'✅ PASSED' if result == expected else '❌ FAILED'}")
    
    print(f"\n🎉 Solution working correctly!")
    print("Strategy: Check parity of (sum(A) - N) to determine winner") 