import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, lagrange


def f(x):
    return 1.0/(1.0 + 25 * x**2)

n = 10
x_interp = np.linspace(-1, 1, n)
y_interp = f(x_interp)

lagrange_poly = lagrange(x_interp, y_interp)
cubic_spline = CubicSpline(x_interp, y_interp)


x_fine = np.linspace(-1, 1, 500)
y_fine = f(x_fine)

y_lagrange = lagrange_poly(x_fine)
y_cubic_spline = cubic_spline(x_fine)

plt.figure(figsize=(8, 8))
plt.plot(x_interp, y_interp, 'ro', label='Sample Points')
plt.plot(x_fine, y_fine, 'g--', label='Actual Function')
plt.plot(x_fine, y_lagrange, 'b-', label='Lagrange Interpolation')
plt.plot(x_fine, y_cubic_spline, 'r-', label='Cubic Spline Interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.close()