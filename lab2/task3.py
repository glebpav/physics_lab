import math

import numpy as np
from matplotlib import pyplot as plt

# [radians]
tan_error = lambda tan: math.radians(2) / (math.cos(math.atan(tan)) ** 2)
tan_error_array = lambda i_array: [tan_error(i) for i in i_array]

# [mTl]
b_error = lambda i: ((i * dk) ** 2 + ((0.012 * i + 0.04) * k) ** 2) ** 0.5
b_error_array = lambda b_array: [b_error(b) for b in b_array]


def get_mse_k_b(x, y):
    Xi = sum(x)
    Xi2 = sum([pow(i, 2) for i in x])
    Yi = sum(y)
    Yi2 = sum([pow(i, 2) for i in y])
    XiYi = sum([x[i] * y[i] for i in range(0, len(x))])
    k = (Yi * Xi - len(x) * XiYi) / (pow(Xi, 2) - len(x) * Xi2)
    b = (XiYi * Xi - Yi * Xi2) / (pow(Xi, 2) - len(x) * Xi2)

    S2 = (len(x) / (len(x) - 2)) * (Yi2 - pow(Yi, 2) - pow(k, 2) * (Xi2 - pow(Xi, 2)))
    SK = S2 / (len(x) * (Xi2 - pow(Xi, 2)))
    dK = math.sqrt(abs(SK))

    return k, b, dK


alpha_1 = [0, -30, -55, -70, -75, -65, -45, -10, 0]
alpha_2 = [0, +30, +55, +70, +75, +65, +45, +10, 0]

i_1 = [0., -20.2, -45.8, -92.0, -117.6, -68.4, -29.9, -6.1, 0.]
i_2 = [0., +19.6, +45.9, +87.2, +115.0, +64.7, +28.0, +6.4, 0.]

k = 0.67
dk = 0.02

tan_1 = [math.tan(math.radians(alpha)) for alpha in alpha_1]
tan_2 = [math.tan(math.radians(alpha)) for alpha in alpha_2]

b0_1 = [k * i for i in i_1]
b0_2 = [k * i for i in i_2]

pair1 = (tan_1 + tan_2, b0_1 + b0_2)

plt.errorbar(pair1[0], pair1[1], yerr=b_error_array(i_1 + i_2), xerr=tan_error_array(pair1[0]), fmt='.', ecolor='red')

k, b, dk = get_mse_k_b(pair1[0], pair1[1])
print(f'Calculated: k={k}, b={b}, dk={dk}')
x = np.linspace(min(pair1[0]), max(pair1[0]), 2)
y = k * x + b
plt.plot(x, y, color='green')

plt.title('График 3.23а.3, "Соответствие магнитного поля тангенсу угла отклонения стрелки"', color='gray', fontsize=9,
          pad=12)

plt.xlabel('tg(α)', color='gray')
plt.ylabel('B₀, мТл', color='gray')
plt.grid(visible=True)
plt.savefig('../assets/lab2/task3.png', dpi=300)
