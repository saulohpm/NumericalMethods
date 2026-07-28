def gauss_method(matrix):

    n = len(matrix)
    
    for i in range(n):

        Li = matrix[i] / matrix[i][i]
        
        for k in range(i + 1, n):
            Lk = matrix[k] - matrix[k][i] * Li
            matrix[k] = Lk

        matrix[i] = Li
        
    return matrix