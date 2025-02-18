import numpy as np
import matplotlib.pyplot as plt

def f_1(x):
    return np.cos(x)

def f_2(x):
    return np.sin(x)

def f_3(x):
    return x

def f_4(x):
    return x**2

def f_5(x):
    return np.log(x)

def g(x, c):
    return c[0] + c[1]*f_1(x) + c[2]*f_2(x) + c[3]*f_3(x) + c[4]*f_4(x) + c[5]*f_5(x)

def construct_A(x_vals, y_vals):
    A = []
    for value in x_vals:
        row = [1, f_1(value), f_2(value), f_3(value), f_4(value), f_5(value)]
        A.append(row)

    A = np.array(A)

    b = np.array([value for value in y_vals]) 
   
    return A, b

def solve_sle(A, b):
    coef = np.linalg.solve(A.T @ A, 
                           A.T @ b)
    return coef

if __name__ == "__main__":
    data = np.loadtxt('./data.csv', delimiter=',')
    x_dat = data[:, 0]  
    y_dat = data[:, 1]  
    # x_dat, y_dat = [0.5, 1, 2, 3,5], [1, 2, 3, 2,4]

    A, b = construct_A(x_dat, y_dat)

    coef = solve_sle(A, b)

    x = np.linspace(np.min(x_dat), np.max(x_dat), 1000)
    y = g(x, coef)

    plt.plot(x, y, 'red',label="Approximated function")
    plt.scatter(x_dat, y_dat, label="Actual data")
    plt.legend()
    plt.show()