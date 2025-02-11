import random

def generate_linear_system(n, min_val=-10, max_val=10):
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    x = [i + 1 for i in range(n)]  
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, b, x

def print_matrix(A, b):
    for i in range(len(A)):
        print(A[i] + [b[i]])
    print()

def gaussian_elimination(A, b):
    n = len(A)
    
    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break
        
        for j in range(i + 1, n):
            if A[j][i] == 0:
                continue
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
        
        print(f"Step {i+1}:")
        print_matrix(A, b)
    
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

def compute_residual(A, x, b):
    n = len(A)
    Ax = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return [Ax[i] - b[i] for i in range(n)]

def generate_hilbert_matrix(n):
    A = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
    x = [i + 1 for i in range(n)]  # Example solution
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, b, x

n = 3
A, b, true_x = generate_linear_system(n)
print("Original System:")
print_matrix(A, b)
solution = gaussian_elimination(A, b)
print("Computed Solution:", solution)
print("Residual:", compute_residual(A, solution, b))

print("\nTesting with Hilbert Matrix:")
A_hilbert, b_hilbert, true_x_hilbert = generate_hilbert_matrix(n)
print_matrix(A_hilbert, b_hilbert)
solution_hilbert = gaussian_elimination(A_hilbert, b_hilbert)
print("Computed Solution:", solution_hilbert)
print("Residual:", compute_residual(A_hilbert, solution_hilbert, b_hilbert))
