import numpy as np

from decomp/SparseMat  import SparseMat
from decomp/svd_decomp import svd_decomp

#generates a random sparse matrix with given "density"
#this is not used in any algorithm but helpful to test and debug the code.
def rand_mat(n, m, density):

    data = np.random.rand(n*m) 
    for i in range(1,len(data)):
        if (np.random.rand() > density):
            data[i] = 0
  
    M = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(data[(m * i) + j])
        M.append(row)
  
    #now do the sparse implementation
    value = []
    col_index = []
    row_index = []


    row_index.append(0)
    for i in range(0,n):
        for j in range(0,m):
            if M[i][j] != 0 :
                value.append(M[i][j])
                col_index.append(j)
        row_index.append(len(col_index))

    return SparseMat(value, col_index, row_index)


#here we generate a random 20x20 matrix and compute the SVD.
def main():

    M = rand_mat(50, 50, .02)

    svd = svd_decomp(M)
    print(svd[0])
    print(svd[1])
    print(svd[2])


if __name__ == '__main__':

    main()

    
