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
even_list = sorted([])
right_dict = dict()
score = []
counter = 0

for i in range(0, goldbah_num):  # список всех чисел в указанном нами промежутке (full_list)
    full_list.append(i)

for j in full_list:  # достаем из (full_list) простые числа и кладем в список (simple_list)
    if check(j):
        simple_list.append(j)

for z in range(4, goldbah_num + 1, 2):  # достаем из (full_list) четные числа и кладем в список (even_list)
    even_list.append(z)


for a in even_list: # проходим по каждому четному числу в диапазоне [4, goldbah_num]
    print(a)
    counter = 0
    for y in simple_list:
        if y < a:
            for x in simple_list:
                if x < a:
                    if x + y == a:
                        counter += 1
                        dd = dict()
                        dd[str(a)] = counter
                        right_dict.update(dd)  # заносим в словарь, если значение счетчика будет = 0 - goldbah wrong


for l in right_dict.values():
    score.append(l)
if 0 in score:  # проверям наличие нуля в значениях
    print("goltbax was wrong!")
else:
    print(f"Goldbah right")


