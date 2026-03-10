
matrix=[]

rows=int(input("Enter Rows Count :: "))
cols=int(input("Enter Column Count :: "))

for i in range(rows):
    row=[]
    for j in range(cols):
        val=int(input("Enter Value :: "))
        row.append(val)
    matrix.append(row)

print("Matrix is :: ")

for r in matrix:
    for c in r:
        print(c,end=" ")
    print()
