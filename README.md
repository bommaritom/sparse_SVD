# Sparse Matrix SVD

## Description: 

A scheme for calculating the SVD of a matrix. Utilizes the sparse structure for data compression using CSR/CRS/Yale format. 

## Dependencies:

Python + Numpy


## Known bugs:

* On occasion completely skips the iterative step. Probably has to do with the way counting non-zero values is handled, i.e. it thinks it is done when it's really not.

(July 2, 2020 : changed the counter logic to try to fix this)
