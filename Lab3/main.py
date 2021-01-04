input_file = open("input.txt")
output_file = open("output.txt", "w")
data = []

for line in input_file:
    data.append([float(x) for x in line.split()])

# по три числа а б с д, вектор входа, точка входа
a = []
for i in range(3):
    a.append(data[0][i])
b = []
for i in range(3):
    b.append(data[1][i])
c = []
for i in range(3):
    c.append(data[2][i])
d = []
for i in range(3):
    d.append(data[3][i])


enter_point = []
for i in range(3):
    enter_point.append(data[4][i])

enter_vector = []
for i in range(3):
    enter_vector.append(data[5][i])

intensity = int(data[6][0])
num_of_mirrors = int(data[7][0])

mirrors = [0] * num_of_mirrors
for i in range(num_of_mirrors):
    mirrors[i] = [0] * 3
    for j in range(3):
        mirrors[i][j] = []
print(mirrors)
for i in range(num_of_mirrors):
    for j in range(3):
        for k in range(3):
            mirrors[i][j].append(data[i + 8][k])

