# Scalar
age = 20

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Scalar multiplication
result = []

for row in matrix:
    new_row = []
    for element in row:
        new_row.append(age * element)
    result.append(new_row)

print("Scalar:", age)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nMatrix after Scalar Multiplication:")
for row in result:
    print(row)