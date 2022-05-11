"""
3. Дано три числа. Знайти суму двох найбільших з них.
Скорий Євген 141
"""

def sum(a, b, c):
    maxim = max(a, b, c)
    minim = min(a, b, c)
    averagenum = (a + b + c) - (maxim + minim)
    sumb = averagenum + maxim
    res = "сума двох найбільших чисел = " + str(sumb)
    return res

x = float(input("Введіть перше число = "))
y = float(input("Введіть друге число = "))
z = float(input("Введіть третє число = "))
result = sum(x, y, z)

print(result)