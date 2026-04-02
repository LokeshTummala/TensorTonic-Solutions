import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    return np.where(x>0, 1/(1+np.exp(-x)),np.exp(x)/(1+np.exp(x)))
    
    """
    If x is very large negative then use e^x/(1+e^x) as the function and if x is a very large positive then it works fine so use the normal one.
    
    Alternative : return np.where(x>0,1/(1+np.exp(-x)),np.exp(x)/(1+np.exp(x)))
    
    """