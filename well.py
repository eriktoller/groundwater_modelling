from plotting import contour_flow_net
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    """
    Create a contour plot of the flow net for a well.
    """

    # Discharge of the well
    q = 1.0 # discharge (m^2/s)
    r = 0.1 # radius of the well (m)
    x0, y0 = 0.0, 0.0 # location of the well
    pi = np.pi

    def well_phi(x, y, xw, yw, q, r):
        """Discharge potential for a well located at (xw, yw)."""
        zw = xw + 1j * yw
        z = x + 1j * y
        omega = (q/(2*pi)) * np.log((z - zw)/r)
        return omega

    # Define the functions for discharge potential and stream function
    phi = lambda x, y: np.real(well_phi(x, y, x0, y0, q, r))  # Discharge potential
    psi = lambda x, y: np.imag(well_phi(x, y, x0, y0, q, r))  # Stream function

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
    plt.title('Flow net for a well')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show the plot
    plt.tight_layout()
    plt.show()

    print("Contour plot generated successfully.")