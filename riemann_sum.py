import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# User input for f(x) function
try:
    fx = input("Enter the function f(x): ")
    f = lambda x: eval(fx)
except Exception as e:
    print("Error:", e)
    print("Please enter a valid function expression.")

def riemann_sum(f, a, b, n):
    """Compute the Riemann sum for the function f over the interval [a, b]"""
    dx = (b - a) / n  # Width of each subinterval
    x = np.linspace(a, b, n+1)  # Partition interval [a, b] into n subintervals
    heights = f(x[:-1])  # Heights of the rectangles using left endpoints
    total_area = np.sum(heights) * dx  # Sum the areas of all rectangles
    return total_area

# Define interval [a, b] and number of subintervals (n)
while True:
    try:
        a, b = map(float, input("Enter the domain values for a and b: ").split())
        break
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        
n = 10

# Plotting the function
x = np.linspace(a, b, 10000)
y = f(x)

# Create the figure and the line
fig, ax = plt.subplots()
line, = ax.plot(x, y, lw=2)

plt.title('Riemann Sum: Approximation of Area under the Curve')

# Creating rectangles
x_bar = np.linspace(a, b, n+1)[:-1]
y_bar = f(x_bar + (b - a) / n)
bar = ax.bar(x_bar, y_bar, width=(b - a) / n, align='edge', alpha=0.3, edgecolor='k')
ax.set_xlabel('Time [s]')

total_area = np.trapz(y, x)
approx_area = riemann_sum(f, a, b, n)
error = total_area - approx_area
textString = f"Area = {total_area:.6f}\n~Area = {approx_area:.6f}\nError = {error:.6f}"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
text = ax.text(0.03, 0.95, textString, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

# Adjust main plot to make room for the slider
fig.subplots_adjust(bottom=0.25)

# Make a horizontal slider to control the precision
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Precision',
    valmin=3,
    valmax=100,
    valinit=n,
    valfmt='%0.0f'
)

# The function to be called anytime the slider's value changes
def update(val):
    global bar, approx_area, error, text
    n = int(val)
    x_bar = np.linspace(a, b, n+1)[:-1]
    y_bar = f(x_bar + (b - a) / n)
    bar.remove()
    bar = ax.bar(x_bar, y_bar, width=(b - a) / n, align='edge', alpha=0.3, edgecolor='k')

    approx_area = riemann_sum(f, a, b, n)
    error = total_area - approx_area
    textString = f"Area = {total_area:.6f}\n~Area = {approx_area:.6f}\nError = {error:.6f}"
    text.set_text(textString)

    fig.canvas.draw_idle()

freq_slider.on_changed(update)

plt.show()