import termtables as tt
import matplotlib.pyplot as plt
from math import sqrt, pow
import numpy as np

"""N_1 = 20
dataset_1 = {
    'expV': [68.1, 31.9, 51.3, 73.1, 95.5, 144, 335, 521, 734, 932, 1450,
             3230, 5610, 7450, 9550, 14100, 33600, 52800, 75700, 93200],
    'T/D': [.01, .01, .005, .002, .002, .001, .0005, .0005, .0002, .0002, .0001, .00005,
            .00002, .00002, .00002, .00001, .000005, .000002, .000002, .000002],
    'D': [6.8, 3.2, 4.0, 7.0, 5.4, 7.0, 6.2, 3.8, 7.0, 5.4,
          7.0, 6.4, 9.2, 6.8, 5.4, 7.2, 6.2, 9.8, 6.8, 5.4]
}"""

"""print('Task #1')

result_1 = {'T': [dataset_1['T/D'][i] * dataset_1['D'][i] for i in range(0, N_1)]}
result_1['V'] = [1 / result_1['T'][i] for i in range(0, N_1)]
result_1['dT'] = [sqrt(0.0009 + pow(0.2 / dataset_1['D'][i], 2)) * result_1['T'][i] for i in range(0, N_1)]
result_1['dV'] = [result_1['dT'][i] / pow(result_1['T'][i], 2) for i in range(0, N_1)]
isOk = [dataset_1['expV'][i] - result_1['dV'][i] <= result_1['V'][i] <= dataset_1['expV'][i] + result_1['dV'][i]
        for i in range(0, N_1)]

table_1 = tt.to_string(
    [[
        i + 1,
        '{:.3g}'.format(dataset_1['expV'][i]),
        '{:.1e}'.format(dataset_1['T/D'][i]),
        dataset_1['D'][i],
        '{:.2e}'.format(result_1['T'][i]),
        '{:.3g}'.format(result_1['V'][i]),
        isOk[i]
    ] for i in range(0, N_1)],
    header=['№', 'expV', 'T/D', 'D', 'T', 'V', 'isOk?']
)
print(table_1 + '\n')

print(result_1['dV'])
"""

print('Task #2')

N_2 = 10
dataset_2 = {
    'V/D': [.2, 1, 1, 2, 2, 2, 5, 5, 5, 5],
    'D': [5.1, 3.4, 5.5, 4.1, 5.4, 7.8, 3.3, 3.8, 4.3, 4.6]
}

result_2 = {'R': [dataset_2['V/D'][i] * dataset_2['D'][i] for i in range(0, N_2)]}
result_2['A'] = [result_2['R'][i] / 2 for i in range(0, N_2)]
result_2['U'] = [result_2['R'][i] / (2 * sqrt(2)) for i in range(0, N_2)]

print(result_2['A'])

table_2 = tt.to_string(
    [[
        i + 1,
        i + 1,
        dataset_2['V/D'][i],
        dataset_2['D'][i],
        '{:.2f}'.format(result_2['R'][i]),
        '{:.2f}'.format(result_2['U'][i])
    ] for i in range(0, N_2)],
    header=['№', 'Del', 'V/D', 'D', 'R', 'U']
)
print(table_2 + '\n')

result_2['dR'] = [sqrt(0.0009 + pow(0.2 / dataset_2['D'][i], 2)) * result_2['R'][i] for i in range(0, N_2)]
result_2['dA'] = [result_2['dR'][i] / 2 for i in range(0, N_2)]
result_2['dU'] = [result_2['dA'][i] / sqrt(2) for i in range(0, N_2)]

print(result_2['dA'])

Xi = sum(range(1, N_2 + 1))
Xi2 = sum([pow(i, 2) for i in range(1, N_2 + 1)])
Yi = sum(result_2['A'])
XiYi = sum([(i + 1) * result_2['A'][i] for i in range(0, N_2)])
k = (Yi * Xi - N_2 * XiYi) / (pow(Xi, 2) - N_2 * Xi2)
b = (XiYi * Xi - Yi * Xi2) / (pow(Xi, 2) - N_2 * Xi2)

print(f'Calculated: k={k}, b={b}')

fig, ax = plt.subplots()
ax.set_xticks(np.arange(0, 11, 0.5), minor=True)
ax.set_yticks(np.arange(0, 11, 0.5), minor=True)
ax.yaxis.grid(True, which='minor')
ax.xaxis.grid(True, which='minor')
plt.grid(True)

plt.xlim(0, 11)
plt.ylim(0, 12)

plt.errorbar(range(1, N_2 + 1), result_2['A'], yerr=result_2['dA'], xerr=[0.5]*len(result_2['dU']), fmt='.', ecolor='red')
x = np.linspace(0, 11, 2)
y = k * x + b
plt.plot(x, y, color='green')

plt.title('График 1а.1, "Зависимость амплитуды сигнала ГЗЧМ от показаний ручки «Амплитуда»"',
          color='gray', fontsize=9, pad=12)
plt.xlabel('Показания ручки ГЗЧМ, Дел', color='gray')
plt.ylabel('Амплитуда, В', color='gray')

plt.show()