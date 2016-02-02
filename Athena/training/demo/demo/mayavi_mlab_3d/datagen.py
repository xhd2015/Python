import numpy as np
from scipy.ndimage import gaussian_filter


def synth_cube(n):
    # Create a data cube for the demo.
    np.random.seed(1235)
    z = np.linspace(-1, 1, n)
    y = np.linspace(-1, 1, n).reshape(n, 1)
    x = np.linspace(-1, 1, n).reshape(n, 1, 1)
    data = (-0.2 * x + 0.35 * y + z
            + 1.2 * np.sin(1.8 * np.pi * (z - 0.2 * x - 0.5 * y) - 1.0)
            + 25 * np.random.randn(n, n, n))
    data = gaussian_filter(data, sigma=(12, 15, 3))
    data = np.arctan(2.5 * data)
    return data
