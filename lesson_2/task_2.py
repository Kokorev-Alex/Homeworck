user_list = list(input(" Введите последовательность  чисел без разделитиля"))
print(user_list)
i = 0
while i + 1 < len(user_list):
    if i % 2 == 0:
        user_list.insert(i, user_list.pop(i + 1))
    i += 1
print(f"Новый список {user_list}")
