import sys
from collections import defaultdict

def solve():
    """
    Reads input and solves the problem, printing the result.
    """
    try:
        # Read input from stdin
        line1 = sys.stdin.readline()
        if not line1: return
        N, M = map(int, line1.split())
        S = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return

    MOD = 998244353

    # --- Helper function to compute state transitions ---
    # The state is an N-bit mask representing the differences in the LCS column.
    def compute_next_mask(mask, char):
        # 1. Reconstruct the LCS column C from the mask
        c_old = [0] * (N + 1)
        for i in range(N):
            c_old[i + 1] = c_old[i] + ((mask >> i) & 1)

        # 2. Compute the new LCS column C_new using standard LCS recurrence
        c_new = [0] * (N + 1)
        for i in range(1, N + 1):
            if S[i - 1] == char:
                c_new[i] = c_old[i - 1] + 1
            else:
                c_new[i] = max(c_new[i - 1], c_old[i])
        
        # 3. Convert C_new back to a mask
        next_mask = 0
        for i in range(N):
            if c_new[i + 1] - c_new[i] == 1:
                next_mask |= (1 << i)
        
        return next_mask

    # --- Precomputation of all state transitions ---
    unique_chars_in_s = sorted(list(set(S)))
    char_to_idx = {ch: i for i, ch in enumerate(unique_chars_in_s)}
    
    # Pick a character not in S for the "other" characters case.
    other_char = 'a'
    if other_char in char_to_idx:
        for i in range(1, 26):
            c = chr(ord('a') + i)
            if c not in char_to_idx:
                other_char = c
                break
    
    transitions = [[0] * (len(unique_chars_in_s) + 1) for _ in range(1 << N)]
    for mask in range(1 << N):
        for i, char in enumerate(unique_chars_in_s):
            transitions[mask][i] = compute_next_mask(mask, char)
        transitions[mask][len(unique_chars_in_s)] = compute_next_mask(mask, other_char)

    # --- Main DP loop ---
    # dp[mask] = count of strings of the current length with this mask
    dp = defaultdict(int)
    dp[0] = 1  # Base case: The empty string has LCS 0, which is mask 0.

    num_other_chars = 26 - len(unique_chars_in_s)

    for _ in range(M):
        dp_new = defaultdict(int)
        for mask, count in dp.items():
            if count == 0:
                continue
            
            # Transitions for characters present in S
            for i in range(len(unique_chars_in_s)):
                next_mask = transitions[mask][i]
                dp_new[next_mask] = (dp_new[next_mask] + count) % MOD
            
            # Transition for all other characters
            if num_other_chars > 0:
                next_mask_other = transitions[mask][len(unique_chars_in_s)]
                dp_new[next_mask_other] = (dp_new[next_mask_other] + count * num_other_chars) % MOD
        
        dp = dp_new

    # --- Final result aggregation ---
    # Group counts by LCS length, which is the number of set bits in the mask.
    ans = [0] * (N + 1)
    for mask, count in dp.items():
        lcs_len = bin(mask).count('1')
        ans[lcs_len] = (ans[lcs_len] + count) % MOD

    print(*ans)

solve()