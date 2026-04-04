import numpy as np

def perplexity(prob_distributions, actual_tokens):
    prob_distributions = np.array(prob_distributions)
    actual_tokens = np.array(actual_tokens)

    N = len(actual_tokens)

    # Extract probabilities of actual tokens
    probs = prob_distributions[np.arange(N), actual_tokens]

    # Avoid log(0)
    probs = np.clip(probs, 1e-10, 1.0)

    # Cross-entropy
    H = -np.mean(np.log(probs))

    # Perplexity
    return np.exp(H)