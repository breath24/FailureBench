def maxActiveSectionsAfterTrade(s):
    """
    Find the maximum number of active sections after performing at most one trade.
    
    A trade involves:
    1. Converting a block of '1's surrounded by '0's to '0's
    2. Converting a block of '0's surrounded by '1's to '1's
    
    Both steps must be possible for a valid trade.
    
    Args:
        s: Binary string
    
    Returns:
        Maximum number of '1's after optimal trade
    """
    n = len(s)
    
    # Augment string with '1's at both ends
    t = '1' + s + '1'
    
    def find_surrounded_blocks(string, target_char, surrounding_char):
        """Find all blocks of target_char surrounded by surrounding_char"""
        blocks = []
        i = 0
        while i < len(string):
            if string[i] == target_char:
                start = i
                while i < len(string) and string[i] == target_char:
                    i += 1
                # Check if surrounded by surrounding_char
                if start > 0 and i < len(string):
                    if string[start-1] == surrounding_char and string[i] == surrounding_char:
                        blocks.append((start, i - 1))
            else:
                i += 1
        return blocks
    
    def apply_trade(string, ones_block, zeros_block):
        """Apply the trade operation: remove ones_block, then convert zeros_block"""
        # Convert to list for easier manipulation
        arr = list(string)
        
        # Step 1: Convert ones to zeros
        if ones_block:
            for i in range(ones_block[0], ones_block[1] + 1):
                arr[i] = '0'
        
        # Step 2: Find zeros surrounded by ones in the modified string
        modified_string = ''.join(arr)
        zeros_blocks = find_surrounded_blocks(modified_string, '0', '1')
        
        # Convert the specified zeros block if it exists and is valid
        if zeros_block:
            for block_start, block_end in zeros_blocks:
                if block_start == zeros_block[0] and block_end == zeros_block[1]:
                    for i in range(block_start, block_end + 1):
                        arr[i] = '1'
                    break
        
        return ''.join(arr)
    
    original_count = s.count('1')
    max_count = original_count
    
    # Find initial blocks of ones surrounded by zeros
    ones_blocks = find_surrounded_blocks(t, '1', '0')
    
    # A valid trade requires BOTH steps to be possible
    # Try all possible trades
    for ones_block in ones_blocks:
        # Apply step 1: convert ones to zeros
        temp_t = apply_trade(t, ones_block, None)
        
        # Find zeros blocks that are now surrounded by ones
        zeros_blocks = find_surrounded_blocks(temp_t, '0', '1')
        
        for zeros_block in zeros_blocks:
            # Apply complete trade
            final_t = apply_trade(t, ones_block, zeros_block)
            
            # Count ones in the original string portion (excluding augmentation)
            final_s = final_t[1:-1]
            count = final_s.count('1')
            max_count = max(max_count, count)
    
    return max_count


# Test with provided examples
if __name__ == "__main__":
    test_cases = [
        ("01", 1),
        ("0100", 4),
        ("1000100", 7),
        ("01010", 4)
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result = maxActiveSectionsAfterTrade(s)
        print(f"Example {i}: s = \"{s}\" -> Result: {result}, Expected: {expected}")
        assert result == expected, f"Test case {i} failed!"
    
    print("All test cases passed!")
