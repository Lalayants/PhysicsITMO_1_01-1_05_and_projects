import math

import matplotlib.pyplot as plt
import numpy as np

A = [25, 20, 15, 10, 5]
t = [40.68, 82.27, 132.29, 187.18, 262.17]
plt.scatter(t, A, label="Экспериментальные данные")
plt.legend()
plt.grid()
plt.xlabel("Время t, c")
plt.ylabel("Амплитуда А, градусы")
plt.title("График зависимости амплитуды А(в градусах) \n от времени t(в секундах)")
plt.show()
x = np.linspace(0, 263, 100)
lnA = []
for q in A:
    lnA.append(math.log(q / 30))
plt.scatter(t, lnA, label="ln(A/A_0)")
t_sr = sum(t) / len(t)
lnA_sr = sum(lnA) / len(lnA)
b_up = 0
b_niz = 0
print(lnA)
for k in range(len(t)):
    b_up += (t[k] - t_sr) * (lnA[k] - lnA_sr)
    b_niz += (t[k] - t_sr) ** 2
b = b_up / b_niz
a = lnA_sr - b * t_sr
x = np.linspace(0, 270, 1000)
plt.plot(x, a + b * x, label="ln(A/A_0)= -betta*t, betta = " + str(-b)[0:6] + " tau = " + str(-1 / b)[0:6])

plt.legend()
plt.grid()
plt.xlabel("Время t, c")
plt.ylabel("ln(A/A_0)")
plt.title("График зависимости ln(A/A_0) \n от времени t(в секундах)")
plt.show()
