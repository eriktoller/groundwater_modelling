from plotting import contour_potential, contour_stream_func
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    """
    Create a contour plot of the flow net for two wells in a uniform flow field.
    """

    # Discharge of the well
    qx = 10.0 # discharge in x-direction (m^2/s)
    qy = 2.0 # discharge in y-direction (m^2/s)
    q = 100.0 # discharge (m^2/s)
    r = 0.1 # radius of the well (m)
    x0, y0 = 0.0, 0.0 # location of the first well
    x1, y1 = 5.0, 5.0 # location of the second well
    pi = np.pi

    # Define the functions for discharge potential and stream function
    phi = lambda x, y: -x*qx - y*qy # Placeholder for discharge potential
    psi = lambda x, y: x*qy - y*qx # Placeholder for stream function

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