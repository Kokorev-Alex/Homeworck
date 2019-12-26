#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input("Введите целое положительное число : "))
max_number = 0
i = 10
while number != 0:
    if max_number == 9:
        break
    if number%10>= max_number:
        max_number = number%10
    number = number // 10



print(f"Самое больое число: {max_number}")


