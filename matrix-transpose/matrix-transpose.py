import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    #A = np.array(A)
    #return A.T
    # Alternative Approach 
    return np.array([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])