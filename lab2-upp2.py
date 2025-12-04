# Helper function to find the maximum crossing subarray sum
def max_crossing_sum(A, l, m, r):
    # max left sum
    left_sum = A[m]  # Initialize with the element at the midpoint
    max_left_sum = left_sum
    i = m - 1
    while i >= l:
        left_sum = left_sum + A[i]

        if left_sum > max_left_sum:
            max_left_sum = left_sum
        i -= 1

    # max right sum
    right_sum = A[m + 1] 
    max_right_sum = right_sum
    j = m + 2
    while j <= r:
        right_sum = right_sum + A[j]

        if right_sum > max_right_sum:
            max_right_sum = right_sum
        j += 1
    
    # 3. Crossing Sum
    return max_left_sum + max_right_sum


def max_subarray_sum_dc(A, l=0, r=None):
    # Initialize r for the initial call
    if r is None:
        r = len(A) - 1
        
    if l == r:
        return A[l]

    m = (l + r) // 2

    #conquer
    S_left = max_subarray_sum_dc(A, l, m)
    S_right = max_subarray_sum_dc(A, m + 1, r)
    
    #combine
    S_cross = max_crossing_sum(A, l, m, r)
    
    # return max of the three sums
    max_sum = S_left
    if S_right > max_sum:
        max_sum = S_right
    if S_cross > max_sum:
        max_sum = S_cross
        
    return max_sum

def run_tests():
    print("--- Testing Algorithm 2: Max Subarray Sum (D&C) ---")
    A3_standard = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # Max sum: 18 + 20 + -7 + 12 = 43 (subarray [18, 20, -7, 12])
    print(f"Array: {A3_standard}. Max Sum: {max_subarray_sum_dc(A3_standard)}") # Expected: 43
    
    A3_left = [1, 2, -100, 3, 4] 
    # Max sum: 3 (subarray [1, 2])
    print(f"Array: {A3_left}. Max Sum: {max_subarray_sum_dc(A3_left)}") # Expected: 3
    
    A3_all_negative = [-2, -5, -1, -8] 
    # Max sum: -1 (subarray [-1])
    print(f"Array: {A3_all_negative}. Max Sum: {max_subarray_sum_dc(A3_all_negative)}") # Expected: -1
    print("-" * 40)


run_tests()