def gaussian_elimination(A, b):
    n = len(A)
    
    for i in range(n):
        A[i].append(b[i][0])

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    break
        
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n + 1):  
                A[j][k] -= factor * A[i][k]

            print(f"Step {i+1}:")
            for row in A:
                print(row)
            print()
    
   


A = [[1, 1, 1],
     [3, 2, 1],
     [2, -1, 4]]

b = [[6],
     [10],
     [12]]

solution = gaussian_elimination(A, b)
print("Solution:", solution)
