import numpy as np

def entropy(p):
    """
    :param p: fraction of examples that are correctly classified
    :return: entropy
    """
    if p < 0 or p > 1:
        return 0

    return -p*np.log2(p) - (1-p)*np.log2(1-p)

