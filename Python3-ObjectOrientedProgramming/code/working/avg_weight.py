__author__ = 'Plamen'

from numpy import array, allclose
import warnings

def weighted_average(values, weights):
    """
    Both values and weights are numpy arrays and must be the same length.
    The Sum of the weights must be 1.0
    :param values: numpy array values
    :param weights: numpy array weights
    :return: Return the average of all the values weighted by the weights array
    """

    # Ensure weights sum to (nearly) to 1.0
    weights_total = sum(weights)
    if not allclose(weights_total, 1.0, atol=1e-8):
        msg = "The sum of the weights should ussually be 1.0." \
              "Instead, it was '%f'" % weights_total
        warnings.warn(msg)

    # Provide useful error message for unequal array lengths
    if len(weights) != len(values):
        msg = "The values (len=%d) and weights (len=%d) arrays" \
              " must have the same length." % (len(values), len(weights))
        raise ValueError(msg)

    # weighted average calculation
    avg = sum(values*weights)/weights_total

    return avg

def main():
    values = array([0.3, 0.3, 0.3, 0.1])
    weights = array([0.25, 0.0, 0.20, 0.30])

    print weighted_average(values, weights)

if __name__ == "__main__":
    main()
