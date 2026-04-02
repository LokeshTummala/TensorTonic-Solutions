import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.isclose(np.sum(p),1):
        return np.dot(x,p)
    else : 
        raise ValueError("ValueError")