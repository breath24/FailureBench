def candidate_func(input_str):
    lines = input_str.strip().split('\n')
    T = int(lines[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(lines[i])
        A, M = solve_case(N)
        results.append(f"{A} {M}")
    
    return '\n'.join(results)

def solve_case(N):
    if N == 1:
        return (123456789, 1)  # Any A works with M=1
    
    # Try to find A and M such that ord_M(A) = N
    # Start with A = 2 and search for suitable M
    A = 2
    for M in range(2, 10000):
        if gcd(A, M) == 1 and check_order(A, M, N):
            return (A, M)
    
    # If A=2 doesn't work, try other values of A
    for A in range(3, 200):
        for M in range(2, 2000):
            if gcd(A, M) == 1 and check_order(A, M, N):
                return (A, M)
    
    # Fallback (shouldn't reach here according to problem statement)
    return (2, N + 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_order(A, M, N):
    """Check if multiplicative order of A modulo M is exactly N"""
    # First check if A^N ≡ 1 (mod M)
    if pow(A, N, M) != 1:
        return False
    
    # Then check that A^d ≢ 1 (mod M) for all proper divisors d of N
    divisors = get_proper_divisors(N)
    for d in divisors:
        if pow(A, d, M) == 1:
            return False
    
    return True

def get_proper_divisors(n):
    """Get all proper divisors of n (divisors less than n)"""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i < n:
                divisors.append(n // i)
    return [d for d in divisors if d < n]


# Test cases
if __name__ == "__main__":
    test_input = """4
3
16
1
55"""
    
    result = candidate_func(test_input)
    print("Output:")
    print(result)
    
    # Verify the results work correctly
    lines = result.strip().split('\n')
    test_lines = test_input.strip().split('\n')
    
    print("\nVerification:")
    for i, line in enumerate(lines):
        A, M = map(int, line.split())
        N = int(test_lines[i + 1])
        
        if N == 1:
            print(f"N={N}: A={A}, M={M} ✅ (Any A works with M=1)")
        else:
            # Verify ord_M(A) = N
            if pow(A, N, M) == 1:
                valid = True
                for d in get_proper_divisors(N):
                    if pow(A, d, M) == 1:
                        valid = False
                        break
                if valid:
                    print(f"N={N}: A={A}, M={M} ✅ (ord_{M}({A}) = {N})")
                else:
                    print(f"N={N}: A={A}, M={M} ❌")
            else:
                print(f"N={N}: A={A}, M={M} ❌") 