import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    N = X.shape[0]

    # Check if 2D
    if X.ndim != 2 or N<2:
        return None

    mean = np.mean(X, axis=0)
    X_centered = X - mean

    cov_mat = (X_centered.T @ X_centered) / (N - 1)

    return cov_mat