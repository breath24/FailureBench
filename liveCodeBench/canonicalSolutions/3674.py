def numberOfSubarrays(nums, k):
    """
    Count the number of subarrays that can be made non-decreasing 
    with at most k increment operations.
    
    Args:
        nums: List of integers
        k: Maximum number of operations allowed
    
    Returns:
        Number of valid subarrays
    """
    n = len(nums)
    count = 0
    
    # Check every possible subarray
    for i in range(n):
        operations = 0
        prev = nums[i]
        
        for j in range(i, n):
            if j > i:
                if nums[j] < prev:
                    # Need to increment nums[j] to match prev
                    operations += prev - nums[j]
                    # nums[j] effectively becomes prev after operations
                else:
                    # nums[j] >= prev, so it becomes the new baseline
                    prev = nums[j]
            
            # If operations needed <= k, this subarray is valid
            if operations <= k:
                count += 1
            else:
                # If this subarray exceeds k operations, 
                # longer subarrays starting at i will also exceed k
                break
    
    return count


# Test with the provided examples
if __name__ == "__main__":
    # Example 1
    nums1 = [6, 3, 1, 2, 4, 4]
    k1 = 7
    result1 = numberOfSubarrays(nums1, k1)
    print(f"Example 1: nums = {nums1}, k = {k1}")
    print(f"Result: {result1}")
    print(f"Expected: 17")
    print()
    
    # Example 2
    nums2 = [6, 3, 1, 3, 6]
    k2 = 4
    result2 = numberOfSubarrays(nums2, k2)
    print(f"Example 2: nums = {nums2}, k = {k2}")
    print(f"Result: {result2}")
    print(f"Expected: 12")


