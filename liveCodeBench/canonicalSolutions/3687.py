from collections import defaultdict

def longestSpecialPath(edges, nums):
    """
    Find the longest special path in a tree where all node values are unique.
    A special path is a downward path from ancestor to descendant.
    
    Args:
        edges: List of [u, v, length] representing tree edges
        nums: List of values at each node
    
    Returns:
        [max_length, min_nodes] where max_length is the longest special path
        and min_nodes is the minimum number of nodes among all longest paths
    """
    n = len(nums)
    graph = defaultdict(list)
    
    # Build adjacency list
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))
    
    max_length = 0
    min_nodes = float('inf')
    
    def dfs(node, parent, used_values, current_length, current_nodes):
        nonlocal max_length, min_nodes
        
        # If current node's value is already used, we can't include it
        if nums[node] in used_values:
            return
        
        # Include current node in the path
        used_values.add(nums[node])
        current_nodes += 1
        
        # Update result with current path
        if current_length > max_length:
            max_length = current_length
            min_nodes = current_nodes
        elif current_length == max_length:
            min_nodes = min(min_nodes, current_nodes)
        
        # Only explore children (downward paths)
        for neighbor, edge_length in graph[node]:
            if neighbor != parent:  # This ensures we only go downward
                dfs(neighbor, node, used_values, current_length + edge_length, current_nodes)
        
        # Backtrack
        used_values.remove(nums[node])
    
    # Start DFS from root (node 0) and explore all downward paths
    def explore_from_node(start_node, parent):
        # Try starting a new path from this node
        dfs(start_node, parent, set(), 0, 0)
        
        # Also try starting paths from all descendants
        for neighbor, _ in graph[start_node]:
            if neighbor != parent:
                explore_from_node(neighbor, start_node)
    
    explore_from_node(0, -1)
    
    # Handle edge case where max_length is 0 (only single nodes are valid)
    if max_length == 0:
        min_nodes = 1
    
    return [max_length, min_nodes]


# Test with provided examples
if __name__ == "__main__":
    # Example 1
    edges1 = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]]
    nums1 = [2,1,2,1,3,1]
    result1 = longestSpecialPath(edges1, nums1)
    print(f"Example 1: edges = {edges1}")
    print(f"nums = {nums1}")
    print(f"Result: {result1}")
    print(f"Expected: [6, 2]")
    print()
    
    # Example 2  
    edges2 = [[1,0,8]]
    nums2 = [2,2]
    result2 = longestSpecialPath(edges2, nums2)
    print(f"Example 2: edges = {edges2}")
    print(f"nums = {nums2}")
    print(f"Result: {result2}")
    print(f"Expected: [0, 1]")
