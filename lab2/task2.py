import math

import matplotlib.pyplot as plt
import numpy as np

# [A]
i_error = lambda i: abs(0.02 * i) + 0.05
i_error_array = lambda i_array: [i_error(i) for i in i_array]

# [mTl]
b_error = lambda b: max(0.01, abs(0.02 * b))
b_error_array = lambda b_array: [b_error(b) for b in b_array]


def get_mse_k_b(x, y):
    Xi = sum(x)
    Xi2 = sum([pow(i, 2) for i in x])
    Yi = sum(y)
    Yi2 = sum([pow(i, 2) for i in y])
    XiYi = sum([x[i] * y[i] for i in range(0, len(x))])

    k = (Yi * Xi - len(x) * XiYi) / (pow(Xi, 2) - len(x) * Xi2)
    b = (XiYi * Xi - Yi * Xi2) / (pow(Xi, 2) - len(x) * Xi2)

    S2 = (len(x) / (len(x) - 2)) * (Yi2 - pow(Yi, 2) - pow(k, 2)*(Xi2 - pow(Xi, 2)))
    SK = S2 / (len(x) * (Xi2 - pow(Xi, 2)))
    dK = math.sqrt(abs(SK))

    return k, b, dK


def draw_plots(pair1, pair2, img_name):
    plt.clf()

    plt.errorbar(pair1[0], pair1[1], yerr=b_error_array(pair1[1]), xerr=i_error_array(pair1[0]), fmt='.', ecolor='red')
    plt.errorbar(pair2[0], pair2[1], yerr=b_error_array(pair2[1]), xerr=i_error_array(pair2[0]), fmt='.', ecolor='red')

    i_tuple = pair1[0] + pair2[0]
    b_tuple = pair1[1] + pair2[1]

    k, b, dk = get_mse_k_b(i_tuple, b_tuple)
    print(f'Calculated: k={k}, b={b}, dk={dk}')
    x = np.linspace(min(i_tuple), max(i_tuple), 2)
    y = k * x + b
    plt.plot(x, y, color='green')

    plt.title('График 3.23а.1, "Градуировка катушек Гельмгольца от "', color='gray', fontsize=9, pad=12)
    plt.xlabel('I, A', color='gray')
    plt.ylabel('B₀, мТл', color='gray')
    plt.grid(visible=True)

    plt.savefig('../assets/lab2/' + img_name, dpi=300)


i_1 = [0., -1., -2, -1.5, -0.5, 0.]
i_2 = [0., +1., +2, +1.5, +0.5, 0.]

b0_1 = [0.00, -0.66, -1.36, -1.02, -0.32, 0.]
b0_3 = [0.01, -0.67, -1.36, -1.1, -0.32, 0.]
b0_2 = [0.01, 0.70, 1.39, 1.03, 0.34, 0.01]
b0_4 = [0.00, 0.69, 1.38, 1.04, 0.34, 0.01]

pair1 = (i_1, b0_1)
pair2 = (i_2, b0_2)
pair3 = (i_2, b0_3)
pair4 = (i_1, b0_4)

pairs_array = [pair1, pair2, pair3, pair4]

i_1_errors = [i_error(i) for i in i_1]
i_2_errors = [i_error(i) for i in i_2]

draw_plots(pair1, pair2, 'plot1.png')
draw_plots(pair3, pair4, 'plot2.png')