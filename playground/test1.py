import math

def f(x):
    return (x**4) + (3 * x ** 3) + (x** 2 ) - (2 * x) - 0.5

def bisection(a, b, epsilon = 1e-6):
    while abs(b - a) > epsilon:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2



def find_all_root(a,b,epsilon = 1e-6, roots = []):
    ans_roots = roots
    m = (a + b) / 2
    if f(a) * f(b) >= 0:
        find_all_root(a,m,epsilon, ans_roots)
        find_all_root(m,b,epsilon, ans_roots)
    else:
        ans = bisection(a,b,epsilon)
        ans_roots.append(ans)
        # print(ans_roots)

    
    return ans_roots
        
roots = []

print(find_all_root(-3,1,1e-6,roots))

       






            
