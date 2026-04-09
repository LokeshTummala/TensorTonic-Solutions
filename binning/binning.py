import numpy as np 

def binning(values, num_bins):
    values = np.array(values)
    
    min_val = np.min(values)
    max_val = np.max(values)
    
    #  Edge case: all values same
    if min_val == max_val:
        return [0] * len(values)
    range_of_x = max_val - min_val
    w = (range_of_x) / num_bins
    
    bins = np.floor((values - min_val) / w)
    bins = np.clip(bins, 0, num_bins - 1)
    
    return bins.astype(int).tolist()
    