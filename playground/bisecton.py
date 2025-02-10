import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return x**2 - 4
   

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    steps = []
    while abs(b - a) > tol :
        c = (a + b) / 2
        steps.append(c)
        if f(c) == 0:
            return steps
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return steps


fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(-5, 5, 1000)
y = f(x)

steps = bisection_method(f, -5, 5)

def update(frame):
    ax.clear()
    
    ax.plot(x, y, 'b-', linewidth=2, label='f(x)')    
    current_x = steps[frame]
    ax.plot(current_x, f(current_x), 'ro', markersize=10)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.grid(True, alpha=0.3)
    ax.set_title(f'Iteration {frame}: x = {current_x:.10f}')
    ax.set_aspect('equal')
    
    return ax

anim = FuncAnimation(fig, update, frames=len(steps), 
                    interval=500, repeat=False)

anim.save('root_finding.gif', writer='pillow')

plt.close()