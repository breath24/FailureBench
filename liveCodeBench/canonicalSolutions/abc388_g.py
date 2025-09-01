def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    q = int(lines[2])
    
    results = []
    
    for i in range(q):
        l, r = map(int, lines[3 + i].split())
        mochi = a[l-1:r]  # Convert to 0-indexed and extract subarray
        
        # Create indices sorted by value in descending order
        indices = list(range(len(mochi)))
        indices.sort(key=lambda idx: mochi[idx], reverse=True)
        
        used = [False] * len(mochi)
        count = 0
        
        # Process elements from largest to smallest
        for idx in indices:
            if used[idx]:
                continue
            
            # Find the largest element that can be placed on top of mochi[idx]
            best_partner = -1
            for j in range(len(mochi)):
                if used[j] or j == idx:
                    continue
                if mochi[j] * 2 <= mochi[idx]:
                    if best_partner == -1 or mochi[j] > mochi[best_partner]:
                        best_partner = j
            
            # If we found a valid partner, pair them
            if best_partner != -1:
                used[idx] = True
                used[best_partner] = True
                count += 1
        
        results.append(str(count))
    
    return '\n'.join(results)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": """11
1 1 2 3 4 4 7 10 11 12 20
5
2 5
3 8
7 11
1 2
1 11""",
            "expected": """2
3
1
0
5"""
        },
        {
            "input": """24
127 148 170 174 258 311 331 414 416 436 517 523 532 587 591 638 660 748 760 776 837 857 972 984
15
7 11
8 9
8 13
12 15
9 23
1 17
8 12
1 5
6 17
3 7
12 19
13 18
7 22
1 12
14 15""",
            "expected": """0
0
0
0
2
6
0
1
1
0
0
0
3
5
0"""
        }
    ]
    
    print("Running test cases...")
    for i, test_case in enumerate(test_cases, 1):
        result = candidate_func(test_case["input"])
        expected = test_case["expected"]
        
        print(f"\nTest case {i}:")
        print("Result:")
        print(result)
        print("Expected:")
        print(expected)
        print(f"Match: {result == expected}")
        
        if result != expected:
            print("❌ FAILED")
            break
        else:
            print("✅ PASSED")
    else:
        print("\n🎉 All test cases passed!") 