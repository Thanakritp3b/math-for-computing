import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)

def gen_x(a, b, n):
    x = []
    for i in range(n):
        x.append(a + (b - a) * i / (n - 1))
    return x

def get_matrix(x):
    matrix = []
    for i in range(len(x)):
        row = []
        for j in range(len(x)):
            row.append(x[i] ** j)
        matrix.append(row)
    return matrix
        
def evaluate_polynomial(coefficients, x_values):
    n = len(coefficients)
    y_values = np.zeros_like(x_values)
    for i in range(n):
        y_values += coefficients[i] * np.power(x_values, i)
    return y_values


def lagrange_polynomial(x, y, x_values):
    n = len(x)
    y_values = np.zeros_like(x_values)
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (x_values - x[j]) / (x[i] - x[j])
        y_values += l * y[i]
    return y_values

def plot_polynomial(x, y, coefficients, x_values, y_real):
    y_values = evaluate_polynomial(coefficients, x_values)
    plt.scatter(x, y, label='Data Points')
    plt.plot(x_values, y_values, label='Polynomial Interpolation')
    plt.plot(x_values, y_real, color='red', label='Interpolated Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Polynomial Interpolation')
    plt.show()


matrix_size = 9
num_points = 14
x = gen_x(-matrix_size, matrix_size, num_points)
y = [f(xi) for xi in x]
matrix = get_matrix(x)
# print(matrix)
solve_matrix = np.linalg.solve(matrix, y)
print(solve_matrix)
interp_x = np.linspace(-10, 10, 100)
real_y = [f(xi) for xi in interp_x]
plot_polynomial(x, y, solve_matrix, interp_x, real_y)


coefficients = lagrange_polynomial(x, y, interp_x)
print(coefficients)
plt.figure()  
lagrange_y = lagrange_polynomial(x, y, interp_x)
plt.scatter(x, y, label='Data Points')
plt.plot(interp_x, lagrange_y, label='Lagrange Interpolation')
plt.plot(interp_x, real_y, color='red', label='True Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lagrange Interpolation')
plt.show()






