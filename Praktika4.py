import random
print("praktika :igra v kamni")
print("\\\\\\\\\\\Да начнётся игра в камни!///////")

def igra(n):
    while n > 0:
        print("Осталось камней:", n)
        a=input("Выберите количество камней от 1 до 3: ")
        try:
            a=int(a)
        except ValueError:
            print("Вы должны ввести целое число камней")
            exit(0)
        if a>3 or a<1:
            print("Введите значение от 1 до 3")
            exit(0)
        n -= a
        if n <= 0:
            print("Победа!")
            exit(0)
        comp=random.randint(1,3)
        if comp==1:
            print(f"Противник забрал {comp} камень")
        else:
            print(f"Противник забрал {comp} камня")
        n-=comp
        if n <= comp:
            print("Вы проиграли")
            exit(0)

n = random.randint(4, 30)
igra(n)
