import math

import matplotlib.pyplot as plt
import numpy as np

epsilon = [[2.91028, 5.56698, 7.70881, 10.11316],
           [2.28023, 3.96121, 5.93193, 6.65929],
           [1.58862, 2.67524, 4.22275, 5.25522],
           [1.34125, 2.07716, 3.05549, 4.24508],
           [0.95746, 1.70215,
            2.50781,
            3.43428], [0.78901,
                       1.29976,
                       1.79497,
                       2.38052]
           ]
epslon_err = [[0.31655237,
               0.60781614,
               0.8602261,
               1.10349791],
              [0.25049862,
               0.43079444,
               0.65146813,
               0.72446086],
              [0.17271327,
               0.29184836,
               0.471214,
               0.58272766],
              [0.14588517,
               0.22788757,
               0.33297779,
               0.4617814],
              [0.10414314,
               0.18530531,
               0.27292148,
               0.37356939],
              [0.08577197,
               0.14925932,
               0.19550633,
               0.25886129]

              ]
momentum = [[0.05989356,
             0.10855964,
             0.1567999,
             0.2044129],
            [0.05998255,
             0.10897332,
             0.15746446,
             0.20610662],
            [0.06008024,
             0.10930462,
             0.1581037,
             0.20679515],
            [0.06011518,
             0.10945869,
             0.15854026,
             0.2072905], [0.06016939,
                          0.10955531,
                          0.15874509,
                          0.20768811], [0.06019318,
                                        0.10965897,
                                        0.1590117,
                                        0.20820485]]
momentum_err = [[0.00660608,
                 0.01185249,
                 0.01707966,
                 0.02224618],
                [0.0066159,
                 0.01189765,
                 0.01715193,
                 0.02243046,
                 ],
                [0.00662667,
                 0.01193382,
                 0.01722157,
                 0.02250546], [0.00663052,
                               0.01195064,
                               0.01726908,
                               0.0225593],
                [0.0066365,
                 0.01196119,
                 0.01729139,
                 0.02260257], [0.00663913,
                               0.01197251,
                               0.01732043,
                               0.02265881]]
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
print("N J Ftp")
j = []
for i in range(len(epsilon)):
    plt.errorbar(epsilon[i], momentum[i], momentum_err[i], epslon_err[i], 'none', color=color[i])
    eps_sr = sum(epsilon[i]) / len(epsilon[i])
    mom_sr = sum(momentum[i]) / len(momentum[i])
    b_up = 0
    b_niz = 0
    for k in range(len(epsilon[i])):
        b_up += (epsilon[i][k] - eps_sr) * (momentum[i][k] - mom_sr)
        b_niz += (epsilon[i][k] - eps_sr) ** 2
    b = b_up / b_niz
    a = mom_sr - b * eps_sr
    x = np.linspace(0, max(epsilon[i]) + max(epsilon[i]) * 0.05)
    plt.plot(x, a + b * x, label='N = ' + str(i + 1) + " J = " + str(b)[0:5] + " Fтр = " + str(a)[0:7], color=color[i])
    j.append(b)
    print(i, b, a)
plt.legend()
plt.grid()
plt.ylabel("Момент силы, H*м")
plt.xlabel("Угловое ускорение маятника, рад/с^2")
plt.title("График зависимости момента силы \nот углового ускорения маятника")
plt.show()
r = [0.078, 0.103, 0.128, 0.153, 0.178, 0.203]
Rsq = [x ** 2 for x in r]
plt.scatter(Rsq, j, label="Полученные данные")
b_up = 0
b_niz = 0
rsq_sr = sum(Rsq) / len(Rsq)
j_sr = sum(j) / len(j)
for k in range(len(r)):
    b_up += (Rsq[k] - rsq_sr) * (j[k] - j_sr)
    b_niz += (Rsq[k] - rsq_sr) ** 2
b = b_up / b_niz
a = j_sr - b * rsq_sr
print(b_niz)
x = np.linspace(0, 0.045)
plt.plot(x, a + b * x, label='МНК, m = ' + str(b // 0.0001 * 0.0001 / 4) + ', j =' + str(a // 0.0001 * 0.0001))
plt.plot(x, a + 1.632 * x, '>', markersize=5, label='J - МНК; m - табличное')
plt.plot(x, 0.008 + 1.632 * x, '-.', label='Табличные значения m и J')
print('m = ' + str(b) + ', j =' + str(a))
plt.legend()
plt.grid()
plt.ylabel("Момент инерции, кг*м,2")
plt.xlabel("Расстояние в квадрате до грузов, м^2")
plt.title("График зависимости момента инерции \nот расстояние в квадрате до грузов")
plt.show()

dd = 0
for k in range(len(r)):
    dd += (j[k] - (a + Rsq[k] * b)) ** 2
sigma_gr = math.sqrt(dd / (16 * b_niz * 4))
sigma_mi = math.sqrt(dd / 4 * (1 / 6 + rsq_sr ** 2 / b_niz))
print(sigma_gr * 2.57, sigma_mi * 2.57)
