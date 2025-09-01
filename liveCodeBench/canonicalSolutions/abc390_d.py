def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    
    def generate_partitions(arr, start=0, current_partition=[]):
        """Generate all non-empty partitions of arr"""
        if start == len(arr):
            if current_partition:  # Only yield non-empty partitions
                yield current_partition[:]
            return
        
        # Try adding arr[start] to each existing part
        for i in range(len(current_partition)):
            current_partition[i].append(arr[start])
            yield from generate_partitions(arr, start + 1, current_partition)
            current_partition[i].pop()
        
        # Try creating a new part with arr[start]
        current_partition.append([arr[start]])
        yield from generate_partitions(arr, start + 1, current_partition)
        current_partition.pop()
    
    xor_values = set()
    
    for partition in generate_partitions(a):
        xor_val = 0
        for part in partition:
            part_sum = sum(part)
            xor_val ^= part_sum
        xor_values.add(xor_val)
    
    return str(len(xor_values))


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": """3
2 5 7""",
            "expected": "3"
        },
        {
            "input": """2
100000000000000000 100000000000000000""",
            "expected": "2"
        },
        {
            "input": """6
71 74 45 34 31 60""",
            "expected": "84"
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