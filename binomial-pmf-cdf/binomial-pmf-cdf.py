import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    PMF = comb(n,k)*(p**k)*(1-p)**(n-k)
    CDF = 0 
    for i in range(k+1):
        CDF = CDF + comb(n,i)*(p**i)*(1-p)**(n-i)
    return PMF,CDF