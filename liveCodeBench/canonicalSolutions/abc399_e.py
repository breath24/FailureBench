def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    S = lines[1]
    T = lines[2]
    
    # Check feasibility: each character in S must consistently map to same character in T
    char_mapping = {}
    for i in range(N):
        if S[i] in char_mapping:
            if char_mapping[S[i]] != T[i]:
                return "-1"
        else:
            char_mapping[S[i]] = T[i]
    
    # Build directed graph of transformations needed
    graph = {}
    for char, target in char_mapping.items():
        if char != target:
            graph[char] = target
    
    if not graph:
        return "0"  # No transformations needed
    
    # Find cycles and calculate operations
    visited = set()
    operations = 0
    
    def find_cycle_length(start):
        path = []
        current = start
        positions = {}
        
        while current not in positions:
            if current not in graph:
                # Path ends at a character that doesn't need to change
                return len(path), 0
            positions[current] = len(path)
            path.append(current)
            current = graph[current]
        
        # Found a cycle
        cycle_start_pos = positions[current]
        path_length = cycle_start_pos
        cycle_length = len(path) - cycle_start_pos
        
        return path_length, cycle_length
    
    for start_char in graph:
        if start_char in visited:
            continue
        
        path_length, cycle_length = find_cycle_length(start_char)
        
        # Mark all nodes in this component as visited
        current = start_char
        component_nodes = []
        while current not in visited and current in graph:
            visited.add(current)
            component_nodes.append(current)
            current = graph[current]
        
        if cycle_length == 0:
            # No cycle, just a path
            operations += len(component_nodes)
        elif cycle_length == 1:
            # Self-loop (character maps to itself, but we already filtered these out)
            operations += len(component_nodes)
        else:
            # Actual cycle of length > 1 needs one extra operation
            operations += len(component_nodes) + 1
    
    return str(operations)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "6\nafbfda\nbkckbb",
            "expected": "4"
        },
        {
            "input": "4\nabac\nabac",
            "expected": "0"
        },
        {
            "input": "4\nabac\nabrc", 
            "expected": "-1"
        },
        {
            "input": "4\nabac\nbcba",
            "expected": "4"
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
            # Debug info for failed cases
            lines = test_case["input"].strip().split('\n')
            N = int(lines[0])
            S = lines[1]
            T = lines[2]
            print(f"S: {S}")
            print(f"T: {T}")
            
            char_mapping = {}
            for j in range(N):
                char_mapping[S[j]] = T[j]
            print(f"Mapping: {char_mapping}")
            break
        else:
            print("✅ PASSED")
    else:
        print("\n🎉 All test cases passed!") 