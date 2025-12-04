
import time
import random
import matplotlib.pyplot as plt

# --- Provided Functions ---

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


# --- Helper Functions for Timing ---

def measure_time(func, inputs):
    """Measures the execution time for a function over a set of inputs."""
    times = []
    for arr in inputs:
        start_time = time.time()
        func(arr[:]) # Pass a copy to avoid mutating the original
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def generate_inputs(start, end, step, max_value=1000):
    """Generates lists of increasing size with random numbers."""
    sizes = list(range(start, end, step))
    inputs = []
    for size in sizes:
        # Create an array of random integers
        arr = [random.randint(1, max_value) for _ in range(size)]
        inputs.append(arr)
    return sizes, inputs

# --- Execution ---

if __name__ == "__main__":
    # Define the range of input sizes (n)
    MIN_SIZE = 50
    MAX_SIZE = 1000
    STEP = 50

    sizes, inputs = generate_inputs(MIN_SIZE, MAX_SIZE, STEP)


    print("Measuring check_sum_n2 (O(n^2))...")
    # For check_sum_n2, we must call it with the original array to trigger the initial sort
    # Since the input arrays are already copies in the measure_time loop, this is fine.
    time_check_sum_n2 = measure_time(check_sum_n2, inputs)

    # --- Plotting the Results ---

    # Calculate theoretical O(n^2) curve for comparison
    # We normalize the theoretical curve to match the scale of the measured time
    # This involves finding a scaling constant (k)
    k_check = time_check_sum_n2[-1] / (MAX_SIZE**2)
    
    theoretical_n2_check = [k_check * (n**2) for n in sizes]

    plt.figure(figsize=(12, 6))


    # Plot for check_sum_n2
    plt.subplot(1, 2, 2)
    plt.plot(sizes, time_check_sum_n2, 'ro', label='Measured Time')
    plt.plot(sizes, theoretical_n2_check, 'g-', label='Theoretical $O(n^2)$')
    plt.title('check_sum_n2 Time Complexity: $O(n^2)$')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()