def gaussian_elimination(A, b):
    n = len(A)
    
    for i in range(n):
        A[i].append(b[i][0])


       
    


A = [[1, 1, 1],
     [3, 2, 1],
     [2, -1, 4]]

b = [[6],
     [10],
     [12]]

solution = gaussian_elimination(A, b)
print("Solution:", solution)
