from plotting import contour_potential, contour_stream_func
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    """
    This script generates a flow net for a well using contour plots of discharge potential and stream function.
    """

    # Discharge of the well
    q = 1.0 # discharge (m^2/s)
    r = 0.1 # radius of the well (m)
    pi = np.pi

    # Define the functions for discharge potential and stream function
    phi = lambda x, y: 0*x + 0*y # Placeholder for discharge potential
    psi = lambda x, y: 0*x + 0*y # Placeholder for stream function

    # Create the figure window
    fig = plt.figure(figsize=(8, 8))

    # Define the range for x and y axes
    xrange = (-10, 10)
    yrange = (-10, 10)

    # Generate contour plots
    contour_potential(xrange, yrange, function=phi)
    contour_stream_func(xrange, yrange, function=psi)
    plt.axis('equal') # Set equal scaling for both axes (this is important for flow nets)

    # Add labels and title
    plt.legend()
    plt.title('Flow net for a well')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show the plot
    plt.tight_layout()
    plt.show()

    print("Contour plot generated successfully.")