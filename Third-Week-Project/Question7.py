#Write a program to find the sum of diagonal elements of a matrix. (Hint: use 2D List)

def sumOfDiagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Check if the matrix is square
    if rows != cols:
        print("Error: Matrix is not square. Diagonal sum not possible.")
        return None
    
    diagonal_sum = 0
    
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    
    return diagonal_sum

# Example: Define a 3x3 matrix
matrix = [
    [1, 2, 7],
    [4, 3, 5],
    [4, 6, 1]
]

# Calculate and print the sum of diagonal elements
result = sumOfDiagonal(matrix)

if result is not None:
    print(f"The sum of diagonal elements is: {result}")
