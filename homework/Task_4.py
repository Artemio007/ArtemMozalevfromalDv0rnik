
# True если число простое и больше 4

def check(num):
    k, count = 1, 0
    while k <= num:
        if num % k == 0:
            count += 1
        k += 1
    if count == 2:
        return True
    else:
        return False


goldbah_num = int(input())
full_list = sorted([])
simple_list = sorted([])
counter = 0
for i in range(4, goldbah_num):
    full_list.append(i)

for j in full_list:
    if check(j):
        simple_list.append(j)
print(simple_list)
for y in simple_list:
    for x in simple_list:
        if x + y == goldbah_num:
            counter += 1

print(f"Goldbah right {counter} times")