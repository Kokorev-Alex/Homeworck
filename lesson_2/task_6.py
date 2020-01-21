goods = []
all_name = []
all_price = []
all_qua = []
all_uni = []
n = 1
while True:
    name = input(f"ввдетие наименование товара № {n}")
    all_name.append(name)
    price = input(f"введите цену товара№ {n}")
    all_price.append(price)
    qua = input(f"Введите количество№ {n}")
    all_qua.append(qua)
    uni = input(f"введите единицы измерения товара № {n}")
    all_uni.append(uni)
    tup = {"название": name, "цена": price, "количество": qua, "eд": uni}
    dic = (n, tup)
    goods.append(dic)
    n += 1
    print(goods)
    end_check = input("Для завершения ввода данных  наберите 'qqq'")
    if end_check == "qqq":
        break

analys = {"название": all_name, 'цена': all_price, 'количество': all_qua, "единицы": all_uni}
print(analys)
