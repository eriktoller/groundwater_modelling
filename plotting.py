import numpy as np
import matplotlib.pyplot as plt

def contour_potential(xrange, yrange, function, levels=10, num_points=100, labels=True):
    """
    Generates a contour plot for a given function over specified x and y ranges.

    Parameters
    ----------
    xrange : tuple
        A tuple specifying the range of x values (xmin, xmax).
    yrange : tuple
        A tuple specifying the range of y values (ymin, ymax).
    function : callable
        A function that takes two arguments (x, y) and returns a z value.
    levels : int, optional
        The number of contour levels to plot (default is 10).
    num_points : int, optional
        The number of points to generate in each dimension (default is 100).
    labels : bool, optional
        Whether to label the contour lines (default is True).

    Returns
    -------
    X, Y, Z : ndarray
        Meshgrid arrays for x, y, and the computed z values.
    """
    # Validate input
    _validate_input_contour(xrange, yrange, function, levels, num_points, labels)

    # Create a grid of x and y values
    x = np.linspace(xrange[0], xrange[1], num_points)
    y = np.linspace(yrange[0], yrange[1], num_points)
    X, Y = np.meshgrid(x, y)

    # Compute the result values using the provided function
    res = function(X, Y)

    # Plot the contour
    plt.contour(X, Y, res, colors='red', linestyles='dashed', linewidths=1, levels=levels)
    if labels:
        # Create an invisible red line for the legend
        plt.plot(xrange[0], yrange[0], color='red', ls='dashed', lw=1, label='Equipotential Lines')

    return None


def contour_stream_func(xrange, yrange, function, levels=10, num_points=100, labels=True):
    """
    Generates a contour plot for a given function over specified x and y ranges.

    Parameters
    ----------
    xrange : tuple
        A tuple specifying the range of x values (xmin, xmax).
    yrange : tuple
        A tuple specifying the range of y values (ymin, ymax).
    function : callable
        A function that takes two arguments (x, y) and returns a z value.
    levels : int, optional
        The number of contour levels to plot (default is 10).
    num_points : int, optional
        The number of points to generate in each dimension (default is 100).
    labels : bool, optional
        Whether to label the contour lines (default is True).

    Returns
    -------
    X, Y, Z : ndarray
        Meshgrid arrays for x, y, and the computed z values.
    """
    # Validate input
    _validate_input_contour(xrange, yrange, function, levels, num_points, labels)

    # Create a grid of x and y values
    x = np.linspace(xrange[0], xrange[1], num_points)
    y = np.linspace(yrange[0], yrange[1], num_points)
    X, Y = np.meshgrid(x, y)

    # Compute the result values using the provided function
    res = function(X, Y)

    # Plot the contour
    plt.contour(X, Y, res, colors='blue', linestyles='solid', linewidths=1, levels=levels)
    if labels:
        # Create an invisible red line for the legend
        plt.plot(xrange[0], yrange[0], color='blue', lw=1, label='Streamlines')

    return None


def _validate_input_contour(xrange, yrange, function, levels, num_points, labels):
    """
    Validates the input parameters for contour plotting functions.

    Parameters
    ----------
    xrange : tuple
        A tuple specifying the range of x values (xmin, xmax).
    yrange : tuple
        A tuple specifying the range of y values (ymin, ymax).
    function : callable
        A function that takes two arguments (x, y) and returns a z value.
    levels : int
        The number of contour levels to plot.
    num_points : int
        The number of points to generate in each dimension.
    labels : bool
        Whether to label the contour lines.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid.
    """
    # Check that the input are the correct types
    # Check that num_points is a positive integer
    if not isinstance(num_points, int) or num_points <= 0:
        raise ValueError("num_points must be a positive integer.")

    # Check that labels is a boolean
    if not isinstance(labels, bool):
        raise ValueError("labels must be a boolean value.")

    # Check that levels is a positive integer
    if not isinstance(levels, int) or levels <= 0:
        raise ValueError("levels must be a positive integer.")

    # Check that the ranges are tuples of length 2
    if not isinstance(xrange, tuple) or not isinstance(yrange, tuple):
        raise ValueError("xrange and yrange must be tuples.")
    if len(xrange) != 2 or len(yrange) != 2:
        raise ValueError("xrange and yrange must be tuples of length 2.")

    # Check that the function is callable
    if not callable(function):
        raise ValueError("function must be a callable that takes two arguments (x, y).")

    # Check that the function can be called with two arguments
    try:
        test_x = np.array([[0]])
        test_y = np.array([[0]])
        function(test_x, test_y)
    except Exception as e:
        raise ValueError("function must be callable with two arguments (x, y).") from e

    assert xrange[0] < xrange[1], "Invalid xrange: xmin must be less than xmax."
    assert yrange[0] < yrange[1], "Invalid yrange: ymin must be less than ymax."