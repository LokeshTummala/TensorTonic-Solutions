import numpy as np

def geometric_pmf_mean(k, p):
    if not (0 < p <= 1):
        raise ValueError("p must be in (0, 1]")
    
    mean = 1 / p
    
    PMF = [((1 - p) ** (i - 1)) * p for i in k]
    
    return (np.array(PMF), mean)