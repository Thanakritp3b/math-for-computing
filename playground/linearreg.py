import matplotlib.pyplot as plt

def Model(beta, _X): #return list of each y_pred
    X = [[x, 1] 
         for [x] in _X ]       # n row 2 col
    # beta = [[m], 
    #         [c]]             # 2 row 1 col # column vector
    #Res = [[..]..]          # n row 1 col
    def mult(A, B): # A, B = matrix
        if (len(A[0]) != len(B)):
            return "ERROR"
        R = [[0] * len(B[0]) for i in range(len(A))]
        for i in range(len(R)):
            for j in range(len(R[i])):
                for k in range(len(B)):
                    R[i][j] += A[i][k] * B[k][j]
        return R
    return mult(X, beta)

def diff(Y_pred, Y_true):
    D = [[None] for i in range(len(Y_pred))] # D : column vector of difference between component of Y_pred and Y_true
    for i in range(len(Y_pred)):
        D[i][0] = Y_pred[i][0] - Y_true[i][0]
    return D

def Loss(Y_pred, Y_true):
    L = 0
    for [val] in diff(Y_pred, Y_true):
        L += val ** 2
    return L

def grad_w_lr(X, Y_pred, Y_true, lr):
    D = diff(Y_pred, Y_true)
    F_m = sum([D[i][0] * X[i][0] for i in range(len(D))]) # partial derivative with respect to m
    F_c = sum([val * 1 for [val] in D]) # partial derivative with respect to c
    return [[F_m * lr], 
            [F_c * lr]] # column vector (gradient) of y = mx + c if m , c is variable

def update(beta, val):
    for i in range(2):
        beta[i][0] -= val[i][0]
    return beta


def train(X, Y_true):
    beta = [[1],
            [1]]
    lr = 0.01
    L_prev = 1e9
    L_cur = -1e9
    while ( abs(L_prev - L_cur) >= 1e-6): #epsilon
        L_prev = L_cur

        Y_pred = Model(beta, X)
        val = grad_w_lr(X, Y_pred, Y_true, lr)
        beta = update(beta, val)

        L_cur = Loss(Y_pred, Y_true)
    return beta, L_cur 

data = [(1, 2), 
        (4, 7), 
        (5, 8), 
        (7, 9),
        (3, 6)]

X = [[x_i] 
     for (x_i, y_i) in data] # column vector
Y_true = [[y_i] 
          for (x_i, y_i) in data] # column vector

beta, loss = train(X, Y_true)
m, c = beta[0][0], beta[1][0]

plt.figure(figsize=(10,6))
plt.scatter([x for [x] in X], [y for [y] in Y_true])
plt.plot([0, 8], [m * 0 + c, m * 8 + c], label=f"y = {m:.2f}x + {c:.2f}")
plt.legend(loc='upper left')
plt.show()
print(loss / len(data))