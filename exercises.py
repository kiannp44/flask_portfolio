age1 = 20
age2 = 16
def swap(age1, age2):

    if age1 > age2:
        age2, age1 = age1, age2

    return age1, age2

print(swap(age1, age2))

def print_matrix(matrix):
    print("classical nested loops using ij indexes")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
