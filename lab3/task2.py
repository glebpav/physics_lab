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

    plt.errorbar(x_array, y_array * 1000, yerr=y_error_array * 1000, xerr=x_error_array * 1000, fmt='.', ecolor='red')

    k, b, dk = get_mse_k_b(x_array, y_array)
    print(f'Calculated: k={k}, b={b}, dk={dk}')
    x = np.linspace(min(x_array), max(x_array), 2)
    y = k * x + b
    plt.plot(x, y * 1000, color='green')

    plt.title('График 14.1, "Зависимость напряжённости вихревого электрического поля от частоты"', color='gray', fontsize=9, pad=12)
    plt.xlabel('ν, Гц', color='gray')
    plt.ylabel('E, мВ/м', color='gray')
    plt.grid(visible=True)

    plt.savefig('../assets/lab3/plot1', dpi=300)


value_2_pi_r_N = 2 * 3.14 * 0.015 * 10

table = {
    'nu': np.array([150, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),  # frequency
    'vd': np.array([.025, .025, .025, .025, .025, .025, .025, .025, .025, .025]),  # volt per division
    'dc': np.array([0.4, 0.5, 0.7, 0.9, 1.2, 1.3, 1.6, 1.9, 2.3, 2.6])  # division count
}

table['sp'] = table['vd'] * table['dc']  # scope
table['V'] = table['sp'] / 2
table['E'] = table['V'] / value_2_pi_r_N

table['e_rel_error'] = np.sqrt(0.02 ** 2 + (0.2 / table['dc']) ** 2)
table['e_abs_error'] = table['E'] * table['e_rel_error']

print(f"E: {table['E'] * 1000}\n")
print(f"E relevant error: {table['e_rel_error']}\n")
print(f"E absolute error: {table['e_abs_error'] * 1000}\n")

draw_plots(table['nu'], table['E'], table['e_abs_error'], table['e_abs_error'])


