import numpy as np

# Input: Size of the square matrix
n = int(input())
# Input: Read the matrix A
A = []
for _ in range(n):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)

eigenvalues, eigenvectors = np.linalg.eig(A)


eigenvectors_inverse = np.linalg.inv(eigenvectors)

# Print the results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

print("\nInverse of Eigenvectors:")
print(eigenvectors_inverse)
