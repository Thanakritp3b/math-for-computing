import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2 - 4
    ##return (x-1)**3

def f_prime(x):
    return 2* x
    ##return 3*(x-1)**2

def g(x):
    return - f(x)/4 + x
    ##return -0.1*f(x) + x

def find_root_newton(f, f_prime, x0, num_iter):
    x_vals = []
    x = x0
    for i in range(num_iter):
        if abs(f_prime(x)) < 1e-10:  
            break
        x_vals.append(x)
        x = x - f(x)/f_prime(x)
    return x_vals

def find_root_bisect(f, a, b, num_iter):
    x_vals = []
    if f(a) * f(b) > 0:
        print("Bisection method: Invalid interval")
        return []
        
    for i in range(num_iter):
        c = (a + b)/2
        x_vals.append(c)
        
        if abs(f(c)) < 1e-10:
            break
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return x_vals

def find_root_fixed_point(g, x0, num_iter):
    x_vals = []
    x = x0
    for i in range(num_iter):
        x_vals.append(x)
        x = g(x)
        if abs(x - x_vals[-1]) < 1e-10:
            break
    return x_vals

a = -2
b = 4
x0 = 4 
num_iter = 100
real_solution = 2.0

newton_vals = find_root_newton(f, f_prime, x0, num_iter)
bisect_vals = find_root_bisect(f, a, b, num_iter)
fixed_point_vals = find_root_fixed_point(g, x0, num_iter)

def calculate_errors(x_vals, real_solution):
    return [abs(x - real_solution) for x in x_vals]

newton_errors = calculate_errors(newton_vals, real_solution)
bisect_errors = calculate_errors(bisect_vals, real_solution)
fixed_point_errors = calculate_errors(fixed_point_vals, real_solution)

plt.figure(figsize=(10, 6))

methods_to_plot = {
    'Newton': (newton_errors, 'b-'),
    'Bisection': (bisect_errors, 'r-'),
    'Fixed Point': (fixed_point_errors, 'g-')
}

for method_name, (errors, style) in methods_to_plot.items():
    if errors:  
        plt.plot(errors, style, label=method_name)

plt.yscale('log')
plt.grid(True)
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Root Finding Methods Convergence')
plt.legend()
plt.show()

for method_name, (errors, _) in methods_to_plot.items():
    if errors:
        print(f"{method_name} final error: {errors[-1]:.2e}")