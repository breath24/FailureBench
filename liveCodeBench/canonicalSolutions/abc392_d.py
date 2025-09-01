from collections import Counter
from fractions import Fraction

def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    
    dice = []
    for i in range(1, N + 1):
        parts = list(map(int, lines[i].split()))
        K = parts[0]
        faces = parts[1:]
        dice.append(faces)
    
    max_prob = Fraction(0)
    
    for i in range(N):
        for j in range(i + 1, N):
            dice1 = dice[i]
            dice2 = dice[j]
            
            count1 = Counter(dice1)
            count2 = Counter(dice2)
            
            # Calculate probability using exact fractions
            prob = Fraction(0)
            for num in count1:
                if num in count2:
                    prob += Fraction(count1[num], len(dice1)) * Fraction(count2[num], len(dice2))
            
            if prob > max_prob:
                max_prob = prob
    
    # Convert to float and format with exactly 15 decimal places
    return f"{float(max_prob):.15f}"


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": "3\n3 1 2 3\n4 1 2 2 1\n6 1 2 3 4 5 6",
            "expected": "0.333333333333333"
        },
        {
            "input": "3\n5 1 1 1 1 1\n4 2 2 2 2\n3 1 1 2",
            "expected": "0.666666666666667"
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
