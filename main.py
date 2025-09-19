def check_number():
    try:
        num = int(input("Введите число: "))

        if num % 2 == 0:
            print(f"Число {num} является чётным")
        else:
            print(f"Число {num} является нечётным")

        if num % 5 == 0:
            print(f"Число {num} делится на 5 без остатка")
        else:
            print(f"Число {num} НЕ делится на 5 без остатка")

        if num % 7 == 0:
            print(f"Число {num} делится на 7 без остатка")
        else:
            print(f"Число {num} НЕ делится на 7 без остатка")

        if abs(num) % 10 == 3:
            print(f"Число {num} оканчивается на цифру 3")
        else:
            print(f"Число {num} НЕ оканчивается на цифру 3")

    except ValueError:
        print("Ошибка! Пожалуйста, введите целое число.")


check_number()