import numpy as np
from scipy import ndimage

__all__ = ['rand_array','smooth_image']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return ndimage.gaussian_filter(a, sigma=sigma)

def square(x):
    return y