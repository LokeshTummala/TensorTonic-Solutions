import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    n = len(x)
    x = np.array(x)
    mean = np.mean(x)
    s_squared = (1/(n-1))*(np.sum((x-mean)**2))
    s = np.sqrt(s_squared)
    return s_squared,s