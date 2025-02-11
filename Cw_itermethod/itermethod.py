import random

def jacobi(matrix, result, x0, real_solution):
    n = len(matrix)  
    x_new = [0] * n 

    for i in range(n):
        sum = result[i]
        for j in range(n):
            if i != j:
                sum -= matrix[i][j] * x0[j]
        x_new[i] = sum / matrix[i][i]
    
    if x_new == real_solution:
        return x_new
    print(x_new)
    
    return jacobi(matrix, result, x_new, real_solution)

def seidel_iter(matrix, result, x_new,real_solution):
    n = len(matrix)
    for i in range(n):
        sum = result[i]
        for j in range(n):
            if i != j:
                sum -= matrix[i][j] * x_new[j]
        x_new[i] = sum / matrix[i][i]

    if x_new == real_solution:
        return x_new
    print(x_new)

    return seidel_iter(matrix, result,x_new ,real_solution)


def generate_linear_system(n, min_val=-10, max_val=10):
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        A[i][i] = random.randint(row_sum + 1, row_sum + 10)  # Ensure diagonal dominance
        
    x = [i + 1 for i in range(n)]
    
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    
    return A, b, x


# def check_diagonal_dominance(matrix):
#     n = len(matrix)
#     for i in range(n):
#         row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
#         if abs(matrix[i][i]) <= row_sum:
#             return False
#     return True



matrix, result, real_solution = generate_linear_system(8)

print(f"matrix : {matrix}")
print(f"res : {result}")
print(f"real : {real_solution}")

x0 = [0] * len(matrix)
# print(f"x0 : { x0 }")
# print(jacobi(matrix, result, x0, real_solution))
print(seidel_iter(matrix, result, x0,real_solution))