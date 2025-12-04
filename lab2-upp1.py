def check_sum_n2(A, n=None):
    #checks for x + y = z in A using a O(n^2) incremental approach 
    #and sorting the prefix A[0...n-1] in place.

    if n is None: #check len of n
        k = 0
        while True:
            try:
                _ = A[k]
                k += 1
            except IndexError:
                break
            n = k
    
    # base case
    if n < 3:
        return 0

    # check the subarray A[0...n-2], return 1 if true
    if check_sum_n2(A, n - 1):
        return 1
    
    # incremental sort (insertion sort step - O(n))
    # A[0...n-2] is sorted. insert A[n-1] into the correct spot in A[0...n-1]
    
    # store the element to be inserted
    a_n = A[n - 1] 
    j = n - 2
    
    # move elements to the right if greater than a_n  
    while j >= 0 and A[j] > a_n:
        A[j + 1] = A[j] 
        j -= 1
        
    # insert a_n into its sorted position
    A[j + 1] = a_n

    # check Triplet (x + y = z)
    # and if A[i] + A[j] = A[n-1] for i, j < n-1 using two pointers on the sorted prefix
    z = A[n - 1]
    
    i = 0         # left pointer
    j = n - 2     # right
    
    while i < j:
        S = A[i] + A[j]
        
        if S == z:
            # x + y = z, where z is the new sorted element
            return 1
        elif S < z:
            i += 1    # larger sum
        else: # S > z
            j -= 1    # smaller sum
            
    return 0



def check_sum_n3(A, n=None):
    #O(n^3)
    #initialize n if not provided
    if n is None:
        n = len(A)
    
    if n < 3:
        return 0

    #recursively check the subarray A[0...n-2]
    if check_sum_n3(A, n - 1):
        return 1
    
    #check if the new element A[n-1] completes a triplet with elements from A[0...n-2]
    a_n = A[n - 1]
    
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1:
            if i != j:
                a_i = A[i]
                a_j = A[j]
                #check the three possibilities for x + y = z:
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
        
    #no triplet found involving the new element or in the subproblem
    return 0

#helper function TA BORT o fixa linjär på o(n^2)
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

def run_tests():
    print("* testing Algorithm 1.1: Theta(n^3) x + y = z")
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