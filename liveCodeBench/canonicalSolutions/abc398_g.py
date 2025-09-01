def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    N, M = map(int, lines[0].split())
    
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for i in range(1, M + 1):
        u, v = map(int, lines[i].split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Find connected components and their bipartitions
    visited = [False] * N
    total_part_A = 0
    total_part_B = 0
    isolated_vertices = 0
    
    for i in range(N):
        if not visited[i]:
            if not adj[i]:  # Isolated vertex
                isolated_vertices += 1
                visited[i] = True
                continue
                
            # BFS to find component and bipartition
            component = []
            color = [-1] * N
            queue = [i]
            color[i] = 0
            visited[i] = True
            
            while queue:
                u = queue.pop(0)
                component.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 1 - color[u]
                        queue.append(v)
            
            # Count vertices in each part of this component
            part_A = sum(1 for v in component if color[v] == 0)
            part_B = len(component) - part_A
            total_part_A += part_A
            total_part_B += part_B
    
    # Optimally assign isolated vertices to maximize total edges
    # We want to maximize (total_part_A + x) * (total_part_B + (isolated_vertices - x))
    # This is maximized when x ≈ (isolated_vertices + total_part_B - total_part_A) / 2
    
    best_max_edges = 0
    for x in range(isolated_vertices + 1):
        final_A = total_part_A + x
        final_B = total_part_B + (isolated_vertices - x)
        max_edges = final_A * final_B
        best_max_edges = max(best_max_edges, max_edges)
    
    # Total number of moves = maximum possible edges - current edges
    total_moves = best_max_edges - M
    
    if total_moves % 2 == 1:
        return "Aoki"
    else:
        return "Takahashi"


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "4 3\n1 2\n2 3\n3 4",
            "expected": "Aoki"
        },
        {
            "input": "4 2\n1 2\n3 4", 
            "expected": "Takahashi"
        },
        {
            "input": "9 5\n2 9\n2 3\n4 6\n5 7\n1 8",
            "expected": "Aoki"
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