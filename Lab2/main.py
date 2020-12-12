import math

input_file = open("input.txt")
output_file = open("output.txt", "w")
data = []

for line in input_file:
    data.append([float(x) for x in line.split()])

our_ship = [data[0][0], data[0][1]]
keel = [data[1][0], data[1][1]]
mast = [data[2][0], data[2][1]]
enemy_ship = [data[3][0], data[3][1]]
new_enemy_ship = [0, 0]
# привели со в виду с центром в в нашем корабле
enemy_ship[0] = enemy_ship[0] - our_ship[0]
enemy_ship[1] = enemy_ship[1] - our_ship[1]
# посчитали угол между осью х и килем
our_ship[0] = math.asin(keel[1] / math.sqrt(keel[0] * keel[0] + keel[1] * keel[1]))
# высчитываем новые координаты с поворот
new_enemy_ship[0] = enemy_ship[0] * math.cos(our_ship[0]) + enemy_ship[1] * math.sin(our_ship[0])
new_enemy_ship[1] = enemy_ship[1] * math.cos(our_ship[0]) - enemy_ship[0] * math.sin(our_ship[0])
new_mast = [0, 0]
new_mast[0] = mast[0] * math.cos(our_ship[0]) + mast[1] * math.sin(our_ship[0])
new_mast[1] = mast[1] * math.cos(our_ship[0]) - mast[0] * math.sin(our_ship[0])
# считаем угол между килем и врагом
our_ship[0] = math.asin(new_enemy_ship[1] / math.sqrt(new_enemy_ship[0] * new_enemy_ship[0]
                                                  + new_enemy_ship[1] * new_enemy_ship[1]))

if -0.866025 < new_enemy_ship[0] / math.sqrt(new_enemy_ship[0] * new_enemy_ship[0] + new_enemy_ship[1] * new_enemy_ship[1]) < 0.866025:
    if -math.pi / 3 <= math.atan(math.sqrt(new_mast[0] * new_mast[0] + new_mast[1] * new_mast[1])) <= math.pi / 3:
        if new_enemy_ship[1] > 0:
            output_file.writelines("1\n")
        else:
            output_file.writelines("-1\n")
        if (new_enemy_ship[0] > 0) and (new_enemy_ship[1] > 0):
            output_file.writelines(str(round((math.pi / 2 - our_ship[0]) / math.pi * 180, 2)) + "\n")
        elif (new_enemy_ship[0] > 0) and (new_enemy_ship[1] < 0):
            output_file.writelines(str(round((math.pi / 2 + our_ship[0]) / math.pi * 180, 2)) + "\n")
        elif (new_enemy_ship[0] < 0) and (new_enemy_ship[1] > 0):
            output_file.writelines(str(round((-math.pi / 2 + our_ship[0]) / math.pi * 180, 2)) + "\n")
        elif (new_enemy_ship[0] < 0) and (new_enemy_ship[1] < 0):
            output_file.writelines(str(round((-math.pi / 2 - our_ship[0]) / math.pi * 180, 2)) + "\n")
        elif new_enemy_ship[0] == 0:
            output_file.writelines("0.0\n")

        output_file.writelines(str(round(-math.atan(math.sqrt(new_mast[0] * new_mast[0] + new_mast[1] * new_mast[1])), 2) / math.pi * 180) + "\n")
        output_file.writelines("Bye")
    else:
        print("0\n")
else:
    output_file.writelines("0\n")
