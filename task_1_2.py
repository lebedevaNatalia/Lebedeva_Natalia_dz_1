list_of_cubes = []
for i in range(1, 1000, 2):
    list_of_cubes.append(i**3)

for ind, val in enumerate(list_of_cubes):
    sum = 0
    all_sum = 0
    while val > 0:
        sum += val % 10
        val //= 10
    if sum % 7 == 0:
        all_sum += list_of_cubes[ind]
        print(all_sum)

add_list_of_cubes = []
for m in list_of_cubes:
    add_list_of_cubes.append(m + 17)
    all_sum = 0

for ind, val in enumerate(add_list_of_cubes):
    sum = 0
    while val > 0:
        sum += val % 10
        val //= 10
    if sum % 7 == 0:
        all_sum += add_list_of_cubes[ind]
        print(all_sum)