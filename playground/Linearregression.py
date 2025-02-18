import numpy as np
import random
import matplotlib.pyplot as plt

c0 = 1
c1 = 2
a = 0
b = 10
m = 150

# def f(x):
#     return c0 + c1 * x

x = np.loadtxt("x_points.txt")
y = np.loadtxt("y_points.txt")
m = len(x)

# y_noise = y + np.random.normal(0, 1, m)

A = np.zeros((2,2))
B = np.zeros((2))
A[0][0] = m
A[0][1] = sum(x)
A[1][0] = sum(x)
A[1][1] = sum([i**2 for i in x])

B[0] = sum(y)
B[1] = sum([x[i]*y[i] for i in range(m)])

coeff = np.linalg.solve(A, B)

print(coeff)

def P(x):
    return coeff[0] + coeff[1] * x

x_fine = np.linspace(a, b, 100)
# f_fine = f(x_fine)
p_fine = P(x_fine)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Noisy Data')
# plt.plot(x_fine, f_fine, label='True Function')
plt.plot(x_fine, p_fine, label='Least Squares Approximation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Approximation')
plt.show()
plt.close()









