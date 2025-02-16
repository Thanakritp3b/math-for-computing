import numpy as np
import matplotlib.pyplot as plt


h = 1
k = 2


r = 3


def x(t):
    return np.cos(t)
    # return 16* np.sin(t)**3

def y(t):
    # return 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return np.sin(t)


def generate(num_points,interval): 
    n = num_points
    t_vals = []
    for i in range(n):
        t = interval[0] + (interval[1] - interval[0]) * i / (n)
        t_vals.append(t)
    return t_vals

# t_vals = np.linspace(0, 2 * np.pi, 100)
t_vals = generate(20,(0,2*np.pi))
x_vals = x(t_vals)
y_vals = y(t_vals)
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label='Circle')
t_vals = np.linspace(0, 2 * np.pi, 100)
x_vals = x(t_vals)
y_vals = y(t_vals)
plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle')
plt.grid(True)
plt.show()

# print(generate(100,(0,4)))