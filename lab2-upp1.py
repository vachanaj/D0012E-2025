def check_sum_n3(A, n=None):
    #O(n^3)
    # Initialize n if not provided
    if n is None:
        n = len(A)
    
    if n < 3:
        return 0

    # Recursively check the subarray A[0...n-2]
    if check_sum_n3(A, n - 1):
        return 1
    
    #Check if the new element A[n-1] completes a triplet with elements from A[0...n-2]
    a_n = A[n - 1]
    
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
        
    # No triplet found involving the new element or in the subproblem
    return 0

# Helper function 
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
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp
        i += 1

    return A

def check_sum_n2(A, n=None, sorted_A=None):
    #O(n^2)
    if sorted_A is None:
        sorted_A = selection_sort(A[:]) # Create a copy and sort it (O(n^2))
        n = len(sorted_A)
    
    if n < 3:
        return 0

    if check_sum_n2(A, n - 1, sorted_A):
        return 1
    
    z = sorted_A[n - 1]
    
    #Two-Pointer Scan on sorted_A[0...n-2]
    i = 0         
    j = n - 2     
    
    # This loop performs Theta(n) work in the current step.
    while i < j:
        S = sorted_A[i] + sorted_A[j]
        
        if S == z:
            return 1  # Found x + y = z
        elif S < z:
            i += 1    # Need a larger sum
        else: # S > z
            j -= 1    # Need a smaller sum
            
    # exit without finding triplet
    return 0

def run_tests():
    print("--- Testing Algorithm 1.1: Theta(n^3) x + y = z ---")
    A1_yes = [1, 5, 10, 2, 7]  # 2 + 5 = 7
    A1_no = [1, 2, 4, 8, 16]  
    print(f"Array: {A1_yes}. Result (1=True): {check_sum_n3(A1_yes)}") 
    print(f"Array: {A1_no}. Result (1=True): {check_sum_n3(A1_no)}")  
    print("-" * 40)

    print("--- Testing Algorithm 1.2: Theta(n^2) x + y = z ---")
    A2_yes = [10, 5, 1, 7, 2]  # Unsorted array, should work (2 + 5 = 7)
    A2_no = [1, 2, 4, 8, 16]   
    print(f"Array: {A2_yes}. Result (1=True): {check_sum_n2(A2_yes)}") 
    print(f"Array: {A2_no}. Result (1=True): {check_sum_n2(A2_no)}") 
    print("-" * 40)

run_tests()