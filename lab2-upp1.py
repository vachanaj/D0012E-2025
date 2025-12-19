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
        return False

    # check the subarray A[0...n-2], return 1 if true
    if check_sum_n2(A, n - 1):
        return True
    
    # incremental sort (insertion sort step - O(n))
    # A[0...n-2] is sorted. insert A[n-1] into the correct spot in A[0...n-1]
    
    # store the element to be inserted
    a_n = A[n - 1] 
    j = n - 2
    
    # move elements to the right if greater than a_n  
    while j >= 0 and A[j] > a_n:
        A[j + 1] = A[j] 
        j -= 1
    pos = j + 1         # position to insert a_n
    A[pos] = a_n
    
    i = 0         # left pointer
    j = n - 1     # right
    
    #x + y = a_n
    while i < j:
        if i == pos:
            i += 1
            continue
        if j == pos:
            j -= 1
            continue

        S = A[i] + A[j]
        
        if S == a_n:
            return True
        elif S < a_n:
            i += 1    # larger sum
        else: # S > a_n
            j -= 1    # smaller sum

    i = 0         # left pointer
    j = 0         # right
    
    #y - x = new_val (equivalent to x + new_val = y)
    while i < n and j < n:
        if i == pos:
            i += 1
            continue
        if j == pos:
            j += 1
            continue
        if i == j:
            j += 1
            continue

        d = A[j] - A[i]
        
        if d == a_n:
            return True
        elif d < a_n:
            i += 1    # larger sum
        else: 
            i += 1    # smaller sum
            
    return False



def check_sum_n3(A, n=None):
    #O(n^3)
    #initialize n if not provided
    if n is None:
        n = len(A)
    
    if n < 3:
        return False

    #recursively check the subarray A[0...n-2]
    if check_sum_n3(A, n - 1):
        return True
    
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
                    return True
                # 2. a_i + a_n = a_j (z = a_j)
                if a_i + a_n == a_j:
                    return True
                # 3. a_n + a_j = a_i (z = a_i)
                if a_n + a_j == a_i:
                    return True
            j += 1
        i += 1
        
    #no triplet found involving the new element or in the subproblem
    return False


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
    
run_tests()