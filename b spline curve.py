after running if error occurs then in vs code terminal run the code
pip install numpy matplotlib scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# 1. Define the 5 control points from the document
points = np.array([
    [0, 0],
    [1, 2],
    [2, -1],
    [3, 3],
    [4, 0]
])

k = 3  # Degree of the spline: Cubic B-spline
n = len(points)

# 2. Generate the knot vector 
# Note: The knot vector length must be equal to (number of points + degree + 1)
knot_vector = np.linspace(0, 1, n + k + 1)

# 3. Construct the B-Spline interpolation object using Scipy
spline = BSpline(knot_vector, points, k)

# 4. Generate evaluation steps across the parametric range [0, 1]
t_values = np.linspace(0, 1, 100)
curve = spline(t_values)

# 5. Plotting configuration matching your output graph
plt.figure(figsize=(7, 5))

# Plot the generated smooth B-Spline curve
plt.plot(curve[:, 0], curve[:, 1], label="B-Spline Curve", linewidth=1.5)

# Plot the red control points connected by dashed lines
plt.plot(points[:, 0], points[:, 1], 'ro--', label="Control Points")

# Graph aesthetics
plt.title("B-Spline Curve")
plt.legend()
plt.grid(True)

# Display the window frame
plt.show()
