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
    q = 500.0 # discharge (m^2/s)
    r = 0.1 # radius of the well (m)
    x0, y0 = 0.0, 0.0 # location of the first well
    x1, y1 = 5.0, 5.0*0 # location of the second well
    ang = np.angle(qy + 1j* qx)
    x1, y1 = x0+r*2*np.sin(ang), y0+r*2*np.cos(ang)  # location of the second well


    def well_phi(x, y, xw, yw, q, r):
        """Discharge potential for a well located at (xw, yw)."""
        zw = xw + 1j * yw
        z = x + 1j * y
        omega = (q/(2*pi)) * np.log((z - zw)/r)
        return omega

    # Define the functions for discharge potential and stream function
    phi = lambda x, y: -x*qx - y*qy + np.real(well_phi(x, y, x0, y0, q, r) + well_phi(x, y, x1, y1, -q, r))
    psi = lambda x, y: x*qy - y*qx  + np.imag(well_phi(x, y, x0, y0, q, r) + well_phi(x, y, x1, y1, -q, r))

    # Create the figure window
    fig = plt.figure(figsize=(8, 8))

    # Define the range for x and y axes
    xrange = (-10, 10)
    yrange = (-10, 10)

    # Generate contour plots
    contour_flow_net(xrange, yrange, phi_func=phi, psi_func=psi, levels= 50, num_points=1000)
    plt.axis('equal') # Set equal scaling for both axes (this is important for flow nets)

    # Plot the wells
    z0 = r*np.exp(1j * np.linspace(0, 2*pi, 100)) + (x0 + 1j*y0)
    z1 = r*np.exp(1j * np.linspace(0, 2*pi, 100)) + (x1 + 1j*y1)
    plt.plot(z0.real, z0.imag, 'k-', linewidth=2)
    plt.plot(z1.real, z1.imag, 'r-', linewidth=2)

    # Add labels and title
    plt.legend()
    plt.title('Flow net for a well')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show the plot
    plt.tight_layout()
    plt.show()

    print("Contour plot generated successfully.")