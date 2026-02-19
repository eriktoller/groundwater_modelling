from plotting import contour_flow_net
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    """
    Create a contour plot of the flow net for two wells in a uniform flow field.
    """

    # Discharge of the well
    pi = np.pi
    qx = 10.0  # Flow in x-direction
    qy = 1.0  # Flow in y-direction
    q0 = 10.0 # discharge (m^2/day)
    q2 = 5.0 # discharge (m^2/day)
    r = 0.25 # radius of the well (m)
    x0, y0 = 1.0, 2.0 # location of the first well
    x1, y1 = x0, -y0 # location of the second well
    x2, y2 = 2.0, 4.0 # location of the third well
    x3, y3 = 2.0, -4.0 # location of the fourth well


    def well_phi(x, y, xw, yw, q, r):
        """Discharge potential for a well located at (xw, yw)."""
        zw = xw + 1j * yw
        z = x + 1j * y
        z = z**2
        zw = zw**2
        omega = (q/(2*pi)) * np.log((z - zw)/r)
        return omega

    # Define the functions for discharge potential and stream function
    phi0 = 1
    well = lambda x, y: well_phi(x, y, x0, y0, q0, r) - well_phi(x, y, x1, y1, q0, r) + well_phi(x, y, x2, y2, q2, r) - well_phi(x, y, x3, y3, q2, r) + phi0
    head0 = np.real(well(x0, y0+r))
    phi = lambda x, y: np.real(well(x, y))  # Discharge potential
    psi = lambda x, y: np.imag(well(x, y))  # Stream function

    # Create the figure window
    fig = plt.figure(figsize=(8, 8))

    # Define the range for x and y axes
    xrange = (0, 10)
    yrange = (0, 10)

    # Generate contour plots
    contour_flow_net(xrange, yrange, phi_func=phi, psi_func=psi, levels= 20, num_points=500)
    plt.axis('equal') # Set equal scaling for both axes (this is important for flow nets)

    # Add labels and title
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show the plot
    plt.tight_layout()
    plt.show()

    print("Contour plot generated successfully.")