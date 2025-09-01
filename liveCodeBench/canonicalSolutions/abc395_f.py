def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    N, X = map(int, lines[0].split())
    
    teeth = []
    for i in range(1, N + 1):
        u, d = map(int, lines[i].split())
        teeth.append((u, d))
    
    # Calculate original sums
    sums = [u + d for u, d in teeth]
    
    def is_feasible(H):
        # Check if we can achieve U_i + D_i = H with consecutive constraint
        # For each position i, u_i must be in [L_i, R_i]
        ranges = []
        for i in range(N):
            u_orig, d_orig = teeth[i]
            # u_i + d_i = H, so d_i = H - u_i
            # Constraints: 0 ≤ u_i ≤ u_orig and 0 ≤ d_i ≤ d_orig
            # So: 0 ≤ u_i ≤ u_orig and 0 ≤ H - u_i ≤ d_orig
            # Which gives: max(0, H - d_orig) ≤ u_i ≤ min(u_orig, H)
            L = max(0, H - d_orig)
            R = min(u_orig, H)
            if L > R:
                return False
            ranges.append((L, R))
        
        # Check if we can satisfy consecutive constraints
        # Use DP: possible[i] = range of possible values for u_i
        possible = [ranges[0]]
        
        for i in range(1, N):
            L_curr, R_curr = ranges[i]
            L_prev, R_prev = possible[i-1]
            
            # Find intersection of [L_curr, R_curr] with values reachable from previous
            # u_curr must satisfy |u_curr - u_prev| ≤ X for some u_prev in [L_prev, R_prev]
            # So u_curr ∈ [L_prev - X, R_prev + X] ∩ [L_curr, R_curr]
            new_L = max(L_curr, L_prev - X)
            new_R = min(R_curr, R_prev + X)
            
            if new_L > new_R:
                return False
                
            possible.append((new_L, new_R))
        
        return True
    
    # Find maximum feasible H
    max_H = min(sums)
    min_cost = float('inf')
    
    # Try all possible H values from max_H down to 1
    # But to be efficient, we only try critical values
    candidates = set([max_H])
    
    # Add some other candidates around max_H
    for h in range(max(1, max_H - 1000), max_H + 1):
        candidates.add(h)
    
    for H in sorted(candidates, reverse=True):
        if H > max_H:
            continue
            
        if is_feasible(H):
            cost = sum(max(0, s - H) for s in sums)
            min_cost = min(min_cost, cost)
            break  # Since we try H in decreasing order, first feasible is optimal
    
    return str(min_cost)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "4 3\n3 1\n4 1\n5 9\n2 6",
            "expected": "15"
        },
        {
            "input": "4 1000000000\n3 3\n3 3\n3 3\n3 3",
            "expected": "0"
        },
        {
            "input": "4 1\n1000000000 1000000000\n1000000000 1000000000\n1000000000 1000000000\n1 1",
            "expected": "5999999994"
        },
        {
            "input": "15 128\n748 169\n586 329\n972 529\n432 519\n408 587\n138 249\n656 114\n632 299\n984 755\n404 772\n155 506\n832 854\n353 465\n387 374\n567 385",
            "expected": "9460"
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