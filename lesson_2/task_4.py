user_str = input("Введите нескольок слов разделенных пробелом ")
a = list(user_str.split())
for i in range(1, len(a) + 1):
    print(f"{i} ) {a[i - 1][:10:]}")
