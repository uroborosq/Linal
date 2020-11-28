def addition(a, b, xa, xb, ya, yb):
    if (xa == xb) & (ya == yb):
        c = [0] * xa
        for i in range(xa):
            c[i] = [0] * ya

        for i in range(xa):
            for j in range(ya):
                c[i][j] = a[i][j] + b[i][j]
    else:
        return "error"

    return c


def transpone(a, x, y):
    c = [0] * y
    for i in range(y):
        c[i] = [0] * x

    for i in range(y):
        for j in range(x):
            c[i][j] = a[j][i]

    return c


def multiplication_on_const(a, t, x, y):
    c = [0] * x
    for i in range(x):
        c[i] = [0] * y

    for i in range(x):
        for j in range(y):
            c[i][j] = t * a[i][j]

    return c


def multiplication(a, b, xa, xb, ya, yb):
    if ya == xb:
        c = [0] * xa
        for i in range(xa):
            c[i] = [0] * yb
        for i in range(xa):
            for j in range(yb):
                for k in range(ya):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
        return c
    else:
        return "error"


cin = open('input.txt')
cout = open("output.txt", "w")

data = []
for line in cin:
    data.append([float(x) for x in line.split()])


a = data[0][0]
b = data[0][1]

height_of_first = int(data[1][0])
width_of_first = int(data[1][1])

first = [0] * height_of_first

for i in range(height_of_first):
    first[i] = [0] * width_of_first


for i in range(height_of_first):
    for j in range(width_of_first):
        first[i][j] = data[2][i * width_of_first + j]

height_of_second = int(data[3][0])
width_of_second = int(data[3][1])

second = [0] * height_of_second
for i in range(height_of_second):
    second[i] = [0] * width_of_second

for i in range(height_of_second):
    for j in range(width_of_second):
        second[i][j] = data[4][i * width_of_second + j]

height_of_third = int(data[5][0])
width_of_third = int(data[5][1])

third = [0] * height_of_third

for i in range(height_of_third):
    third[i] = [0] * width_of_third


for i in range(height_of_third):
    for j in range(width_of_third):
        third[i][j] = data[6][i * width_of_third + j]

height_of_fourth = int(data[7][0])
width_of_fourth = int(data[7][1])

fourth = [0] * height_of_fourth

for i in range(height_of_fourth):
    fourth[i] = [0] * width_of_fourth

for i in range(height_of_fourth):
    for j in range(width_of_fourth):
        fourth[i][j] = data[8][i * width_of_fourth + j]

height_of_fifth = int(data[9][0])

width_of_fifth = int(data[9][1])

fifth = [0] * height_of_fifth

for i in range(height_of_fifth):
    fifth[i] = [0] * width_of_fifth

for i in range(height_of_fifth):
    for j in range(width_of_fifth):
        fifth[i][j] = data[10][i * width_of_fifth + j]

# X = C · (α · A + β · B^T))^T· D − F

buf = addition(multiplication_on_const(first, a, height_of_first, width_of_first),
               transpone(multiplication_on_const(second, b, height_of_second,
                                                 width_of_second), height_of_second, width_of_second),
               height_of_first, width_of_second, width_of_first, height_of_second)

if buf != "error":
    buf = multiplication(third, transpone(buf, len(buf), len(buf[0])), height_of_third, len(buf[0]), width_of_third,
                         len(buf))

    if buf != "error":
        buf = multiplication(buf, fourth, len(buf), height_of_fourth, len(buf[0]), width_of_fourth)
        if buf != "error":
            buf = addition(buf, multiplication_on_const(fifth, -1, height_of_fifth, width_of_fifth), len(buf),
                           height_of_fifth, len(buf[0]), width_of_fifth)
            if buf != "error":
                cout.writelines('1\n')
                cout.write(str(len(buf)) + " ")
                cout.write(str(len(buf[0])) + "\n")
                for i in range(len(buf)):
                    for j in range(len(buf[0])):
                        cout.writelines(str(buf[i][j]) + " ")
                exit(0)
cout.write("0")
