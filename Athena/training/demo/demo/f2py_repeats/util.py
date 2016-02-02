import futil2

def find_repeats(arr):
    """Find repeats in arr and return (repeats, repeat_count)
    """    
    v1,v2, n = futil2.dfreps(arr)
    return v1[:n],v2[:n]
        
if __name__ == "__main__":
    import time
    from scipy import stats, float64
    
    a = stats.randint(1, 30).rvs(size=10000)

    repeats, nums = find_repeats(a)
    
    print 'repeats:'
    print repeats
    print 'nums:'
    print nums

