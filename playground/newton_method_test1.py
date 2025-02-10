import math
import matplotlib.pyplot as plt

def f(x):
    return (x**2) - (5 * x) + 4

def df(x):
    return (2 * x) - 5



def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    errors = []
    ans = []
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        err = abs(x_new - x)
        # print(err)
        errors.append(err)
        if abs(x_new - x) < tol:
            # print(f"{i}: {x}")
            break
        x = x_new
        # print(f"{i}: {x}")
        ans.append(x)
    return errors, ans


def plot(errors, ans):
    plt.plot(errors, marker='o', linestyle='-', color='b')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Error vs Iteration')
    plt.show()
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))
    
    # ax1.plot(errors)
    # ax1.set_xlabel('Iteration')
    # ax1.set_ylabel('Error')
    # ax1.set_title('Error vs Iteration')
    
    # ax2.plot(ans)
    # ax2.set_xlabel('Iteration')
    # ax2.set_ylabel('Root')
    # ax2.set_title('Root vs Iteration')
    
    # plt.tight_layout()
    # plt.show()
    

errors, ans = newton_method(f, df, 7)
print(errors)
plot(errors, ans)

