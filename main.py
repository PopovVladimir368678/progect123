import matplotlib.pyplot as plt


def left_sum(n):
    dx = 1 / n
    x = 1
    sum = 0
    for i in range(n):
        sum += 4 ** x
        x += dx
    return dx * sum


def right_sum(n):
    dx = 1 / n
    x = 1 + dx
    sum = 0
    for i in range(n):
        sum += 4 ** x
        x += dx
    return dx * sum


def middle_sum(n):
    dx = 1 / n
    x = 1 + dx / 2
    sum = 0
    for i in range(n):
        sum += 4 ** x
        x += dx
    return dx * sum


n = int(input("Введите количество разбиений: "))
print("Выберите способ:")
print("1 - левые, 2 - правые, 3 - средние")
method = int(input())

if method == 1:
    sum = left_sum(n)
    title = "Интегральная сумма (левые): " + str(sum) + ' Разбиений: ' + str(n)
elif method == 2:
    sum = right_sum(n)
    title = "Интегральная сумма (правые): " + str(sum) + ' Разбиений: ' + str(n)
elif method == 3:
    sum = middle_sum(n)
    title = "Интегральная сумма (средние): " + str(sum) + ' Разбиений: ' + str(n)

x = []
y = []
dx = 1 / n
for i in range(n + 1):
    x.append(1 + i * dx)
    y.append(4 ** (1 + (i * dx)))

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=4^x")

if method == 1:
    for i in range(n):
        x = [1 + i * dx, 1 + (i + 1) * dx, 1 + (i + 1) * dx, 1 + i * dx, 1 + i * dx]
        y = [0, 0, 4 ** (1 + i * dx), 4 ** (1 + i * dx), 0]
        plt.fill(x, y, alpha=0.4, color='b')
elif method == 2:
    for i in range(n):
        x = [1 + i * dx, 1 + (i + 1) * dx, 1 + (i + 1) * dx, 1 + i * dx, 1 + i * dx]
        y = [0, 0, 4 ** (1 + (i + 1) * dx), 4 ** (1 + (i + 1) * dx), 0]
        plt.fill(x, y, alpha=0.4, color='r')
elif method == 3:
    for i in range(n):
        x = [1 + i * dx, 1 + (i + 1) * dx, 1 + (i + 1) * dx, 1 + i * dx, 1 + i * dx]
        y = [0, 0, 4 ** (1 + i * dx + dx / 2), 4 ** (1 + i * dx + dx / 2), 0]
        plt.fill(x, y, alpha=0.4, color='g')

plt.title(title)
plt.show()
