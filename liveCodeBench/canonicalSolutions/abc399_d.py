def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    T = int(lines[0])
    
    results = []
    line_idx = 1
    
    for _ in range(T):
        N = int(lines[line_idx])
        A = list(map(int, lines[line_idx + 1].split()))
        line_idx += 2
        
        # Find positions of each number
        positions = {}
        for i in range(2 * N):
            if A[i] not in positions:
                positions[A[i]] = []
            positions[A[i]].append(i)
        
        # Check which couples are not initially adjacent
        non_adjacent_couples = []
        for num in range(1, N + 1):
            pos1, pos2 = positions[num]
            if abs(pos1 - pos2) != 1:  # Not adjacent
                non_adjacent_couples.append(num)
        
        count = 0
        
        # Check all pairs of non-adjacent couples
        for i in range(len(non_adjacent_couples)):
            for j in range(i + 1, len(non_adjacent_couples)):
                a = non_adjacent_couples[i]
                b = non_adjacent_couples[j]
                
                # Get positions
                i1, i2 = positions[a]
                j1, j2 = positions[b]
                
                # Check if we can make both couples adjacent with one swap
                # There are 4 possible swaps: (i1,j1), (i1,j2), (i2,j1), (i2,j2)
                
                possible = False
                
                # Case 1: Swap (i1, j1) -> a at (j1, i2), b at (i1, j2)
                if abs(j1 - i2) == 1 and abs(i1 - j2) == 1:
                    possible = True
                
                # Case 2: Swap (i1, j2) -> a at (j2, i2), b at (j1, i1)  
                if abs(j2 - i2) == 1 and abs(j1 - i1) == 1:
                    possible = True
                
                # Case 3: Swap (i2, j1) -> a at (i1, j1), b at (i2, j2)
                if abs(i1 - j1) == 1 and abs(i2 - j2) == 1:
                    possible = True
                
                # Case 4: Swap (i2, j2) -> a at (i1, j2), b at (j1, i2)
                if abs(i1 - j2) == 1 and abs(j1 - i2) == 1:
                    possible = True
                
                if possible:
                    count += 1
        
        results.append(str(count))
    
    return '\n'.join(results)


# Test cases
if __name__ == "__main__":
    test_input = """3
3
1 2 3 3 1 2
4
1 1 2 2 3 3 4 4
5
1 2 3 4 5 1 2 3 4 5"""
    
    expected_output = """1
0
4"""
    
    result = candidate_func(test_input)
    print("Result:")
    print(result)
    print("\nExpected:")
    print(expected_output)
    print(f"\nMatch: {result.strip() == expected_output.strip()}")
    
    # Detailed analysis for first test case
    print("\n--- Detailed Analysis for Test Case 1 ---")
    A = [1, 2, 3, 3, 1, 2]
    print(f"Array: {A}")
    
    positions = {}
    for i in range(len(A)):
        if A[i] not in positions:
            positions[A[i]] = []
        positions[A[i]].append(i)
    
    print(f"Positions: {positions}")
    
    # Check couples
    for num in [1, 2, 3]:
        pos1, pos2 = positions[num]
        adjacent = abs(pos1 - pos2) == 1
        print(f"Couple {num} at positions {pos1}, {pos2}: {'Adjacent' if adjacent else 'Not adjacent'}")
    
    # Check pair (1, 2)
    print(f"\nChecking pair (1, 2):")
    i1, i2 = positions[1]  # (0, 4)
    j1, j2 = positions[2]  # (1, 5)
    print(f"Couple 1 positions: {i1}, {i2}")
    print(f"Couple 2 positions: {j1}, {j2}")
    
    print("Checking all 4 swap cases:")
    print(f"Case 1: Swap ({i1},{j1}) -> |{j1}-{i2}|={abs(j1-i2)}, |{i1}-{j2}|={abs(i1-j2)}")
    print(f"Case 2: Swap ({i1},{j2}) -> |{j2}-{i2}|={abs(j2-i2)}, |{j1}-{i1}|={abs(j1-i1)}")
    print(f"Case 3: Swap ({i2},{j1}) -> |{i1}-{j1}|={abs(i1-j1)}, |{i2}-{j2}|={abs(i2-j2)}")
    print(f"Case 4: Swap ({i2},{j2}) -> |{i1}-{j2}|={abs(i1-j2)}, |{j1}-{i2}|={abs(j1-i2)}") 