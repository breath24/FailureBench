import heapq

def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    n, m = map(int, lines[0].split())
    prices = list(map(int, lines[1].split()))
    
    # Priority queue: (cost_of_next_unit, units_already_bought, product_index)
    heap = []
    for i, p in enumerate(prices):
        heapq.heappush(heap, (p, 0, i))  # cost of first unit is p
    
    total_units = 0
    remaining_budget = m
    
    while heap and remaining_budget > 0:
        cost, units_bought, product_idx = heapq.heappop(heap)
        
        if cost > remaining_budget:
            break
            
        # Buy this unit
        remaining_budget -= cost
        total_units += 1
        units_bought += 1
        
        # Calculate cost of next unit
        # If we've bought k units, next unit costs (k+1)^2 * P - k^2 * P = (2k+1) * P
        next_cost = (2 * units_bought + 1) * prices[product_idx]
        heapq.heappush(heap, (next_cost, units_bought, product_idx))
    
    return str(total_units)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": """3 9
4 1 9""",
            "expected": "3"
        },
        {
            "input": """10 1000
2 15 6 5 12 1 7 9 17 2""",
            "expected": "53"
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