user_time = int(input("Введите время в секундах : "))
print(f"Получилось чч:мм:сс {user_time//60**2:02d}:{(user_time//60)%60:02d}:{user_time%60:02d}")
