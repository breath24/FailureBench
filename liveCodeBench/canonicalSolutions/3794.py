def minTime(skill, mana):
    """
    Find the minimum time required to brew all potions properly.
    
    Args:
        skill: List of skill levels for each wizard
        mana: List of mana capacities for each potion
    
    Returns:
        Minimum time to complete all potions
    """
    n = len(skill)
    m = len(mana)
    
    # Track when each wizard becomes free
    wizard_free_time = [0] * n
    
    for j in range(m):
        # Find the earliest start time for potion j
        min_start_time = 0
        cumulative_time = 0
        
        # For each wizard, determine when this potion can reach them
        for i in range(n):
            # Wizard i needs to start at start_time + cumulative_time
            # Wizard i is free at wizard_free_time[i]
            # So we need start_time + cumulative_time >= wizard_free_time[i]
            # i.e., start_time >= wizard_free_time[i] - cumulative_time
            min_start_time = max(min_start_time, wizard_free_time[i] - cumulative_time)
            cumulative_time += skill[i] * mana[j]
        
        # Update when each wizard becomes free after processing this potion
        start_time = min_start_time
        cumulative_time = 0
        for i in range(n):
            wizard_free_time[i] = start_time + cumulative_time + skill[i] * mana[j]
            cumulative_time += skill[i] * mana[j]
    
    # Return when the last wizard finishes the last potion
    return wizard_free_time[-1]


# Test with provided examples
if __name__ == "__main__":
    # Example 1
    skill1 = [1, 5, 2, 4]
    mana1 = [5, 1, 4, 2]
    result1 = minTime(skill1, mana1)
    print(f"Example 1: skill = {skill1}, mana = {mana1}")
    print(f"Result: {result1}")
    print(f"Expected: 110")
    print()
    
    # Example 2
    skill2 = [1, 1, 1]
    mana2 = [1, 1, 1]
    result2 = minTime(skill2, mana2)
    print(f"Example 2: skill = {skill2}, mana = {mana2}")
    print(f"Result: {result2}")
    print(f"Expected: 5")
    print()
    
    # Example 3
    skill3 = [1, 2, 3, 4]
    mana3 = [1, 2]
    result3 = minTime(skill3, mana3)
    print(f"Example 3: skill = {skill3}, mana = {mana3}")
    print(f"Result: {result3}")
    print(f"Expected: 21")


