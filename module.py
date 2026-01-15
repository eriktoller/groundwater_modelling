import numpy as np

print('This is a module.')

def convert_to_complex(x, y):
    """
    Converts x and y coordinates to a complex number.

    Parameters
    ----------
    x : float
        The x coordinate.
    y : float
        The y coordinate.

    Returns
    -------
    complex_number : complex
        The complex representation of the coordinates.
    """
    return x + 1j * y

if __name__ == "__main__":
    print('Executing module.py directly')
    x = 3.0
    y = 4.0
    complex_number = convert_to_complex(x, y)
    print(f"The complex representation of ({x}, {y}) is {complex_number}")