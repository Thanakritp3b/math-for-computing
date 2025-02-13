import random
import math
import matplotlib.pyplot as plt

def jacobi(matrix, result, x0, real_solution, max_iter=100, tol=1e-10):
    n = len(matrix)  
    x_new = x0.copy()
    iter_count = 0
    errors = []
    x_old = x0.copy()

    while iter_count < max_iter:
        x_old = x_new.copy()
        for i in range(n):
            sum_terms = result[i]
            for j in range(n):
                if i != j:
                    sum_terms -= matrix[i][j] * x_old[j]
            x_new[i] = sum_terms / matrix[i][i]
        
        error = math.sqrt(sum((x_new[i] - x_old[i])**2 for i in range(n)))
        errors.append(error)
        
        print(f"Iteration {iter_count + 1}: {x_new}")
        print(f"Error: {error}")
        
        if error < tol:
            break
            
        iter_count += 1
    
    final_error = math.sqrt(sum((x_new[i] - real_solution[i])**2 for i in range(n)))
    print(f"\nFinal error relative to real solution: {final_error}")
    return x_new, errors

def seidel_iter(matrix, result, x0, real_solution, max_iter=100, tol=1e-10):
    n = len(matrix)
    iter_count = 0
    errors = []
    x_new = x0.copy()
    
    while iter_count < max_iter:
        x_old = x_new.copy()
        for i in range(n):
            sum_terms = result[i]
            for j in range(n):
                if i != j:
                    sum_terms -= matrix[i][j] * x_new[j]
            x_new[i] = sum_terms / matrix[i][i]
        
        error = math.sqrt(sum((x_new[i] - x_old[i])**2 for i in range(n)))
        errors.append(error)
        
        print(f"Iteration {iter_count + 1}: {x_new}")
        print(f"Error: {error}")
        
        if error < tol:
            break
            
        iter_count += 1
    
    final_error = math.sqrt(sum((x_new[i] - real_solution[i])**2 for i in range(n)))
    print(f"\nFinal error relative to real solution: {final_error}")
    return x_new, errors

def generate_linear_system(n, min_val=-10, max_val=10):
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        A[i][i] = random.randint(row_sum + 1, row_sum + 10) 
        
    x = [i + 1 for i in range(n)]  
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    
    return A, b, x

def generate_hilbert_matrix(n):
    A = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
    x = [i + 1 for i in range(n)]  # Example solution
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, b, x


def generate_initial_guess(real_solution, perturbation=0.5):
    return [x + random.uniform(-perturbation, perturbation) for x in real_solution]

def plot_convergence(jacobi_errors, seidel_errors):
    plt.figure(figsize=(10, 6))
    plt.semilogy(range(len(jacobi_errors)), jacobi_errors, 'b-', label='Jacobi')
    plt.semilogy(range(len(seidel_errors)), seidel_errors, 'r-', label='Gauss-Seidel')
    plt.grid(True)
    plt.xlabel('Iteration')
    plt.ylabel('Error (log scale)')
    plt.title('Convergence Comparison')
    plt.legend()
    plt.show()

def main():
    n = 4
    print("\nTesting with diagonally dominant matrix:")
    matrix, result, real_solution = generate_linear_system(n)
    print(f"Matrix: {matrix}")
    print(f"Result vector: {result}")
    print(f"Real solution: {real_solution}")
    
    x0 = generate_initial_guess(real_solution)
    print(f"Initial guess: {x0}")
    
    print("\nJacobi Method:")
    _, jacobi_errors = jacobi(matrix, result, x0.copy(), real_solution)
    
    print("\nGauss-Seidel Method:")
    _, seidel_errors = seidel_iter(matrix, result, x0.copy(), real_solution)
    
    plot_convergence(jacobi_errors, seidel_errors)
    
    print("\nTesting with Hilbert matrix:")
    hilbert_matrix, hilbert_result, hilbert_solution = generate_hilbert_matrix(n)
    x0_hilbert = generate_initial_guess(hilbert_solution)
    
    print("\nJacobi Method (Hilbert):")
    _, jacobi_errors_hilbert = jacobi(hilbert_matrix, hilbert_result, x0_hilbert.copy(), hilbert_solution)
    
    print("\nGauss-Seidel Method (Hilbert):")
    _, seidel_errors_hilbert = seidel_iter(hilbert_matrix, hilbert_result, x0_hilbert.copy(), hilbert_solution)
     
    plot_convergence(jacobi_errors_hilbert, seidel_errors_hilbert)

if __name__ == "__main__":
    main()

"""

[0 , 2 ]
[3 , 5 ]
[2 , 1 ]


"""