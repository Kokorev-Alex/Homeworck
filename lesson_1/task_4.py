#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input("Введите целое положительное число : "))
max_number = 0
i = 10
print(i+i)
while True:
    if max_number == 9:
        break
    if number%10>= max_number:
        max_number = number%10
    if (number//10)%10 >= max_number:
        max_number = (number//10)%10
    if (number//100)%10 >= max_number:
        max_number = (number//100)%10
    if (number//1000)%10 >= max_number:
        max_number = (number//1000)%10
    if (number//10000)%10 >= max_number:
        max_number = (number//10000)%10
    if (number//100000)%10 >= max_number:
        max_number = (number//100000)%10
    if (number//1000000)%10 >= max_number:
        max_number = (number//1000000)%10
    break







print(f"Самое больое число: {max_number}")


