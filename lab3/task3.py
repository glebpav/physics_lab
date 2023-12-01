import math
import numpy as np
from matplotlib import pyplot as plt


def get_mse_k_b(x, y):
    Xi = sum(x)
    Xi2 = sum([pow(i, 2) for i in x])
    Yi = sum(y)
    Yi2 = sum([pow(i, 2) for i in y])
    XiYi = sum([x[i] * y[i] for i in range(0, len(x))])

    k = (Yi * Xi - len(x) * XiYi) / (pow(Xi, 2) - len(x) * Xi2)
    b = (XiYi * Xi - Yi * Xi2) / (pow(Xi, 2) - len(x) * Xi2)

    S2 = (len(x) / (len(x) - 1)) * (Yi2 - pow(Yi, 2) - pow(k, 2)*(Xi2 - pow(Xi, 2)))
    SK = S2 / (len(x) * (Xi2 - pow(Xi, 2)))
    dK = math.sqrt(abs(SK))

    return k, b, dK


def draw_plots(x_array, y_array, x_error_array, y_error_array):
    plt.clf()

    plt.errorbar(x_array, y_array, yerr=x_error_array, xerr=y_error_array, fmt='.', ecolor='red')

    k, b, dk = get_mse_k_b(x_array[0:3], y_array[0:3])
    x = np.linspace(min(x_array[0:3]), max(x_array[0:3]), 2)
    y = k * x + b
    plt.plot(x, y, color='green')

    x = x_array[2:]
    y = y_array[2:]

    n = len(x)  # количество элементов в списках
    s = sum(y)  # сумма значений y
    s1 = sum([1 / x[i] for i in range(0, n)])  # сумма 1/x
    s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # сумма (1/x)**2
    s3 = sum([y[i] / x[i] for i in range(0, n)])  # сумма y/x
    a = (s * s2 - s1 * s3) / (n * s2 - s1 ** 2)  # коэфициент а с тремя дробными цифрами
    b = (n * s3 - s1 * s) / (n * s2 - s1 ** 2)  # коэфициент b с тремя дробными цифрами
    s4 = [a + b / x[i] for i in range(0, n)]  # список значений гиперболической функции
    so = round(sum([abs(y[i] - s4[i]) for i in range(0, n)]) / (n * sum(y)) * 100, 3)  # средняя ошибка аппроксимации

    x1 = np.linspace(min(x_array[2:]), max(x_array[2:]), 200)
    s4 = np.array([a + b / xx for xx in x1])

    plt.plot(x1, s4, color='green')

    plt.title('График 14.2, "Зависимость напряжённости вихревого электрического поля от\nрасстояния до оси соленоида"', color='gray', fontsize=9, pad=12)
    plt.xlabel('r, мм', color='gray')
    plt.ylabel('E, мВ/м', color='gray')
    plt.grid(visible=True)

    plt.savefig('../assets/lab3/plot2', dpi=300)


value_2_pi_N = 2 * 3.14 * 10
solenoid_radius = 0.015

table = {
    'r': np.array([5, 10, 15, 20, 30, 40, 60]),  # ring radius
    'vd': np.array([.025, .025, .025, .025, .025, .025, .025]),  # volt per division
    'dc': np.array([0.5, 1.4, 2.5, 3, 3.5, 3.8, 4])  # division count
}

table['sp'] = table['vd'] * table['dc']  # scope
table['V'] = table['sp'] / 2
table['E'] = table['V'] / (table['r'] * value_2_pi_N)

table['e_rel_error'] = np.sqrt(0.02 ** 2 + (0.2 / table['dc']) ** 2)
table['e_abs_error'] = table['E'] * table['e_rel_error']

print(f"Scope: {table['sp'] * 1000}\n")
print(f"E: {table['E']* 1000}\n")
print(f"E relevant error: {table['e_rel_error']}\n")
print(f"E absolute error: {table['e_abs_error']* 1000}\n")

draw_plots(table['r'], table['E'] * 1000, table['e_abs_error'] * 1000, table['e_abs_error'] * 1000)