from plotting import contour_flow_net
import matplotlib.pyplot as plt

if __name__ == "__main__":
    """
    This script generates a flow net for a uniform flow field using contour plots.
    """

    # Define parameters for the contour plot
    qx = 10.0  # Flow in x-direction
    qy = 1.0  # Flow in y-direction

    # Define the functions for discharge potential and stream function
    phi = lambda x, y: -x*qx - y*qy  # Discharge potential
    psi = lambda x, y: -x*qy + y*qx  # Stream function

    # Create the figure window
    fig = plt.figure(figsize=(8, 8))

    # Define the range for x and y axes
    xrange = (-10, 10)
    yrange = (-10, 10)

    # Generate contour plots
    contour_flow_net(xrange, yrange, phi_func=phi, psi_func=psi)
    plt.axis('equal') # Set equal scaling for both axes (this is important for flow nets)

    # Add labels and title
    plt.legend()
    plt.title('Flow net for uniform flow field')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show the plot
    plt.tight_layout()
    plt.show()

    print("Contour plot generated successfully.")