def transpose_matrix(matrix):
    # Get original matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])

    # Swap rows and columns to flip the matrix
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    # Add values sitting at the exact same row and column
    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(matrix1[r][c] + matrix2[r][c])
        result.append(row)

    return result


def multiply_matrices(matrixA, matrixB):
    m = len(matrixA)
    n = len(matrixA[0])
    p = len(matrixB[0])

    # Calculate row-by-column dot products for matrix multiplication
    result = []
    for r in range(m):
        row = []
        for c in range(p):
            total = 0
            for k in range(n):
                total += matrixA[r][k] * matrixB[k][c]
            row.append(total)
        result.append(row)

    return result


def print_matrix(matrix):
    # Print matrix nicely row by row
    for row in matrix:
        formatted_row = [f"{val:g}" if isinstance(val, (int, float)) else str(val) for val in row]
        print("  ".join(formatted_row))


def read_matrix(rows, cols, name="Matrix"):
    # Take user input row by row and split space-separated values
    matrix = []
    print(f"Enter values for {name} ({rows}x{cols}):")
    for r in range(rows):
        while True:
            try:
                line = input(f"  Enter row {r + 1}: ").strip()
                values = [float(x) for x in line.split()]
                if len(values) != cols:
                    print(f"  Error: Expected {cols} numbers, got {len(values)}. Try again.")
                    continue
                matrix.append(values)
                break
            except ValueError:
                print("  Error: Please enter valid numbers separated by spaces.")
    return matrix


def main():
    # Part A - Transposing Matrix A
    print("=== PART A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = read_matrix(m, n, "Matrix")

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # Part B - Adding two matrices of size M x N
    print("\n=== PART B: Add Two Matrices ===")
    print(f"Reading two matrices of size {m}x{n}...")
    mat1 = read_matrix(m, n, "Matrix 1")
    mat2 = read_matrix(m, n, "Matrix 2")

    sum_matrix = add_matrices(mat1, mat2)
    print("\nMatrix Sum:")
    print_matrix(sum_matrix)

    # Part C - Matrix Multiplication A (M x N) and B (N x P)
    print("\n=== PART C: Multiply Two Matrices ===")
    p = int(input(f"Matrix A is {m}x{n}. Enter number of columns for Matrix B (P): "))
    mat_b = read_matrix(n, p, "Matrix B")

    product_matrix = multiply_matrices(matrix_a, mat_b)
    print("\nMatrix Product (A × B):")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()