import numpy as np
import matplotlib.pyplot as plt

# User input for f(x) function
try:
    fxy = input("Enter the function f(x, y): ")
    f = lambda x, y: eval(fxy)
except Exception as e:
    print("Error:", e)
    print("Please enter a valid function expression.")

def simulate_double_integral():
    """Simulates a double integral and plots the result"""
    while True:
        try:
            x_min, x_max = map(float, input("Enter x-min and x-max (space-separated): ").split())
            y_min, y_max = map(float, input("Enter y-min and y-max (space-separated): ").split())
            break
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    num_points = 100  # Number of points in each dimension

    x = np.linspace(x_min, x_max, num_points)
    y = np.linspace(y_min, y_max, num_points)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Calculate the volume under the surface using the trapezoidal rule
    while True:
        try:
            volume = np.trapz(np.trapz(Z, dx=(x_max - x_min) / (num_points - 1), axis=0), dx=(y_max - y_min) / (num_points - 1))
            break
        except Exception as e:
            print("Error:", e)
            print("Please enter a valid function expression.")
            Z = f(X, Y)

    # Plotting the result
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 3D surface plot
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=1.0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')

    # Set the z-axis limits based on function values
    z_min, z_max = np.min(Z), np.max(Z)
    if z_min >= 0:
        ax.set_zlim(0, z_max)
    elif z_max <= 0:
        ax.set_zlim(z_min, 0)
    else:
        ax.set_zlim(z_min, z_max)

    # Rotate the camera to a different view
    ax.view_init(elev=30, azim=45)  # Change the elev and azim values for different views

    # 2D contour plot (projection on XY-plane)
    ax.contourf(X, Y, Z, zdir='z', offset=0, cmap='viridis', alpha=0.3)

    # Draw dashed lines from surface to base
    ax.plot([x_min, x_min], [y_min, y_min], [0, Z[0, 0]], 'k--')
    ax.plot([x_max, x_max], [y_min, y_min], [0, Z[0, -1]], 'k--')
    ax.plot([x_min, x_min], [y_max, y_max], [0, Z[-1, 0]], 'k--')
    ax.plot([x_max, x_max], [y_max, y_max], [0, Z[-1, -1]], 'k--')

    # Draw boundary dashed lines
    ax.plot(x, y_min * np.ones_like(x), zs=0, linestyle='dashed', color='black')
    ax.plot(x, y_max * np.ones_like(x), zs=0, linestyle='dashed', color='black')
    ax.plot(x_min * np.ones_like(y), y, zs=0, linestyle='dashed', color='black')
    ax.plot(x_max * np.ones_like(y), y, zs=0, linestyle='dashed', color='black')

    plt.title(f"Volume: {volume:.2f}")
    plt.show()

# Run the simulation
simulate_double_integral()