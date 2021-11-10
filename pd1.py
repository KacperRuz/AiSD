def zad1(first_name: str, surname: str):
    return first_name + "." + surname


def zad2(name: str, surname: str):
    return name[0].upper() + "." + surname[0].upper() + surname[1:len(surname)]


def zad3(yearh: str, yearl: str, age: int):
    var = int(yearh+yearl)
    return var - age


def zad4(name: str, surname: str, func):
    return func(name, surname)


def zad5(x: int, y: int):
    if x > 0 and y > 0 and y != 0:
        return x/y
    return 0


def zad6():
    x = 0
    while x < 100:
        try:
            y = int(input("Enter a number: "))
            x = x + y
        except ValueError:
            print("That's not a number.")


def zad7(x: list):
    return tuple(x)


def zad8():
    x = []
    while True:
        inp = input()
        if inp == "stop":
            break
        else:
            x.append(inp)
    return tuple(x)


def zad9(x: int):
    days = ["poniedzialek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    return days[x-1]


def zad10(text: str):
    dist = int((len(text)/2))

    left = text[0:dist].lower()
    right = text[dist+1:len(text)].lower()
    right = right[::-1]

    if left == right:
        return True
    else:
        return False


x1 = zad1("A", "Kowalski")
print(x1)

x2 = zad2("bartosz", "nowak")
print(x2)

x3 = zad3("20", "21", 21)
print(x3)

x4 = zad4("C", "Kowalska", zad1)
print(x4)

x5 = zad5(10, 5)
print(x5)

zad6()

x7 = zad7([1, 2, 3, 4, 5])
print(x7)

x8 = zad8()
print(x8)

x9 = zad9(4)
print(x9)

x10 = zad10("Qaanaaq")
print(x10)
