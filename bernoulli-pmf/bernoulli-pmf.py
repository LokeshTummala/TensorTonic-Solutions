import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array(x)

    # validate x
    if not np.all((x == 0) | (x == 1)):
        raise ValueError("x must contain only 0 and 1")

    # validate p
    if not (0 <= p <= 1):
        raise ValueError("p must be between 0 and 1")

    # PMF
    pmf = (p ** x) * ((1 - p) ** (1 - x))

    # moments
    mean = p
    variance = p * (1 - p)

    return pmf, mean, variance