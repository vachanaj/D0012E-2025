def max_subarray_sum_dc(A, l=0, r=None):
    # Initialize r for the initial call
    if r is None:
        r = len(A) - 1
        
    if l == r:
        x = A[l]
        return x, x, x, x

    # Divide
    m = (l + r) // 2

    # Conquer
    left_total, left_pref, left_suff, left_best = max_subarray_sum_dc(A, l, m)
    right_total, right_pref, right_suff, right_best = max_subarray_sum_dc(A, m + 1, r)

    # Combine
    total = left_total + right_total
    
    # Compute prefix for left half
    prefix = left_pref
    if left_total + right_pref > prefix:
        prefix = left_total + right_pref

    # Compute prefix for right half
    suffix = right_suff
    if right_total + left_suff > suffix:
        suffix = right_total + left_suff

    # Check if best in left, right, or crossing
    best = left_best
    if right_best > best:
        best = right_best
    if left_suff + right_pref > best:
        best = left_suff + right_pref

    return total, prefix, suffix, best
