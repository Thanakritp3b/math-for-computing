import math

def f1(x):
    return math.sqrt(x)

def f2(x):
    return (x**2 - x - 2) 

def f3(x):
    return math.sqrt(x + 2)

def f4(x):
    return (x+ 2) / x 

def fixed_point_iteration(f, x0, alpha,max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = alpha * f(x) + x 
        if abs(x_new - x) < 1e-20:
            print(f"{i}: {x}")
            break
        x = x_new
        print(f"{i}: {x}")
# print("test 1")
# fixed_point_iteration(f3, 2.1)
print("test 2")
fixed_point_iteration(f2, 1.8, -0.4)
# print("test 3")
# fixed_point_iteration(f2, 0.5)
# print("test 4")
# fixed_point_iteration(f3, -0.5)


# x = 2.1

"""
1.8
0.5
-0.5
"""