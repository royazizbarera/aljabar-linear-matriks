import numpy as np
import MatrixOperationsLibrary as mol
import sympy as sp

def get_scale_from_user() -> float:
    '''
    Panduan

    Param:

    Return:
        scalar int
    '''
    scale = float(input("Enter the scale: "))
    return scale


def get_matrix_from_user() -> np.array:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} separated by space: ").split()))
        if len(row) != cols:
            print("Invalid input. Please enter exactly", cols, "elements.")
            return get_matrix_from_user() 
        matrix.append(row)
    return np.array(matrix)


def main():
    print("Enter the matrix:")
    matrix = get_matrix_from_user()

    print("Matrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix") 
    print("5. Inverse Matrix") 
    print("6. Echelon Form Matrix") 
    print("7. Reduced Echelon Form Matrix") 
    print("8. Determinant Matrix") 
    print("9. Multiply By Scalar Matrix")
    print("10. Upper Triangle Matrix")
    choice = input("Enter your choice: ")

    if choice == "1":
        matrix2 = get_matrix_from_user()
        result = mol.add(matrix, matrix2)
    elif choice == "2":
        matrix2 = get_matrix_from_user()
        result = mol.subtract(matrix, matrix2)
    elif choice == "3":
        matrix2 = get_matrix_from_user()
        result = mol.multiply(matrix, matrix2)
    elif choice == "4":
        result = mol.transpose(matrix)
    elif choice == "5":
        result = mol.inverse(matrix)
    elif choice == "6":
        result = mol.echelon(matrix)
    elif choice == "7":
        result = mol.reducedEchelon(matrix)
    elif choice == "8":
        result = np.linalg.det(matrix)
    elif choice == "9":
        scale = get_scale_from_user()
        result = mol.scale(matrix,scale)
    elif choice == "10":
        result,swaps = mol.upperTriangle(matrix)
    else:
        print("Invalid choice.")
        return

    print("Result:")
    print(result)


# Run the main function
main()
