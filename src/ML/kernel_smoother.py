from sklearn.neighbors.kde import KernelDensity
import numpy as np


def kernel_smoother(all_data, bandwidth, sample_size):
    X = np.array(all_data)
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(X)
    return kde.sample(sample_size)
