rating = [7, 6, 5, 4, 4, 3, 3, 2]
print(rating)
while True:
    user_number = int(input("Введите положительное натуральное число:\nДля Выхода введите '999'"))
    if user_number == 999:
        break
    if user_number < 0:
        print("Введите положительное число ")
        continue
    for i, a in enumerate(rating):
        if user_number > a:
            rating.insert(i, user_number)
            break
    else:
        rating.append(user_number)
    print(rating)





