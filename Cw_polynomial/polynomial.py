import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # return np.sin(x) 
    return np.sin(4 * x)

def gen_x(a, b, n):
    return np.random.uniform(a, b, n)

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

def plot_polynomial(x, y, coefficients, x_values, y_real, larrange_y):
    y_values = evaluate_polynomial(coefficients, x_values)
    plt.scatter(x, y, label='Data Points')
    plt.plot(x_values, y_values, label='Polynomial Interpolation')
    plt.plot(x_values, y_real, color='red', label='True Function')
    plt.plot(x_values, larrange_y, 'y--', label='Lagrange Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Polynomial Interpolation')
    plt.show()



interval = (0, 4)
x = gen_x(interval[0], interval[1], 8)
y = [f(xi) for xi in x]
matrix = get_matrix(x)
solve_matrix = np.linalg.solve(matrix, y)

interp_x = np.linspace(interval[0], interval[1], 100)
real_y = [f(xi) for xi in interp_x]

lagrange_y = lagrange_polynomial(x, y, interp_x)
plot_polynomial(x, y, solve_matrix, interp_x, real_y, lagrange_y)
