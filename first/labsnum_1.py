print("Напишите коэффициенты для решения кв. уравнения вида ax^2 + bx + c = 0.")
a = int(input("Введите коэффициент 'a': "))
b = int(input("Введите коэффициент 'b': "))
c = int(input("Введите коэффициент 'c': "))
# ax**2 + bx + c = 0

# дискриминант
d = b**2 - 4*a*c

if d < 0:
    print('Нет корней :(')
elif d == 0:
    print(f"Ваш корень: {(-b)/(2*a)}")
elif d > 0:
    print(f"Ваш первый корень: {(-b + (d**0.5)) / (2 * a)}")
    print(f"Ваш первый корень: {(-b - (d ** 0.5)) / (2 * a)}")