def check_sum_n3(A, n=None):
    """
    Checks for x + y = z in A using a Theta(n^3) incremental approach.
    A is the array, n is the current size to check (default to len(A)).
    """
    # Initialize n if not provided (for the initial call)
    if n is None:
        n = len(A)
    
    # 1. Base Case (Need at least 3 elements)
    if n < 3:
        return 0 # Use 0 for False, 1 for True to avoid built-ins

    # 2. Recursive Step (Incremental)
    # a. Recursively check the subarray A[0...n-2]
    if check_sum_n3(A, n - 1):
        return 1
    
    # c. Check if the new element A[n-1] completes a triplet with elements from A[0...n-2]
    a_n = A[n - 1]
    
    # The check involves iterating over all pairs (A[i], A[j]) in A[0...n-2]
    # This loop performs Theta(n^2) work in the current step.
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1:
            # Elements must be distinct
            if i != j:
                a_i = A[i]
                a_j = A[j]
                
                # Check the three possibilities for x + y = z:
                # 1. a_i + a_j = a_n (z = a_n)
                if a_i + a_j == a_n:
                    return 1
                # 2. a_i + a_n = a_j (z = a_j)
                if a_i + a_n == a_j:
                    return 1
                # 3. a_n + a_j = a_i (z = a_i)
                if a_n + a_j == a_i:
                    return 1
            j += 1
        i += 1
        
    # 3. Final Result: No triplet found involving the new element or in the subproblem
    return 0

# The recurrence relation for this algorithm is T(n) = T(n-1) + O(n^2), 
# which solves to T(n) = O(n^3).

# --- Helper function for sorting (must not use built-in sort) ---
def selection_sort(A):
    n = len(A)
    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            if A[j] < A[min_idx]:
                min_idx = j
            j += 1
        # Swap A[i] and A[min_idx]
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp
        i += 1
    # Note: This function modifies A in place.
    return A

def check_sum_n2(A, n=None, sorted_A=None):
    """
    Checks for x + y = z in A using a Theta(n^2) incremental approach 
    after an initial sorting step.
    A is the original array (passed only for initial call).
    n is the current size to check.
    sorted_A is the globally sorted array (passed through recursion).
    """
    # Pre-Condition: Initial call handles sorting and sets up the recurrence
    if sorted_A is None:
        sorted_A = selection_sort(A[:]) # Create a copy and sort it (O(n^2))
        n = len(sorted_A)
    
    # 2. Base Case
    if n < 3:
        return 0

    # 3. Recursive Step (Incremental)
    # a. Recursively check the subarray A[0...n-2]
    if check_sum_n2(A, n - 1, sorted_A):
        return 1
    
    # b. Check if the new element z = sorted_A[n-1] completes a triplet with elements from sorted_A[0...n-2]
    z = sorted_A[n - 1]
    
    # c. Two-Pointer Scan on sorted_A[0...n-2]
    i = 0         # Left pointer
    j = n - 2     # Right pointer
    
    # This loop performs Theta(n) work in the current step.
    while i < j:
        S = sorted_A[i] + sorted_A[j]
        
        if S == z:
            return 1  # Found x + y = z
        elif S < z:
            i += 1    # Need a larger sum
        else: # S > z
            j -= 1    # Need a smaller sum
            
    # 4. Final Result
    return 0

# The recurrence relation for the recursive part is T(n) = T(n-1) + O(n), 
# which solves to T(n) = O(n^2). The initial O(n^2) sort makes the total complexity Theta(n^2).

def run_tests():
    print("--- Testing Algorithm 1.1: Theta(n^3) x + y = z ---")
    A1_yes = [1, 5, 10, 2, 7]  # 2 + 5 = 7
    A1_no = [1, 2, 4, 8, 16]   # No x + y = z
    print(f"Array: {A1_yes}. Result (1=True): {check_sum_n3(A1_yes)}") # Expected: 1
    print(f"Array: {A1_no}. Result (1=True): {check_sum_n3(A1_no)}")   # Expected: 0
    print("-" * 40)

    print("--- Testing Algorithm 1.2: Theta(n^2) x + y = z ---")
    A2_yes = [10, 5, 1, 7, 2]  # Unsorted array, should work (2 + 5 = 7)
    A2_no = [1, 2, 4, 8, 16]   
    print(f"Array: {A2_yes}. Result (1=True): {check_sum_n2(A2_yes)}") # Expected: 1
    print(f"Array: {A2_no}. Result (1=True): {check_sum_n2(A2_no)}")   # Expected: 0
    print("-" * 40)

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

# Uncomment the line below to run the tests when the script is executed
# run_tests()