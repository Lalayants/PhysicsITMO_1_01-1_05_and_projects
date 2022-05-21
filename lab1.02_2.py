import math
import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

aa = [0.063346847,
      0.151713565,
      0.253090367,
      0.347756058,
      0.469135802]
da = [0.0028, 0.007, 0.019, 0.03, 0.034]
sinn = [0.010,
        0.023,
        0.036,
        0.047,
        0.059]


def summ(abc, bbc):
    s = 0
    for i in range(len(abc)):
        s += abc[i] * bbc[i]
    return s


for k in range(len(aa)):
    aaa = []
    sinnn = []

    for i in range(len(aa)):
        aaa.append(aa[i])
        sinnn.append((sinn[i]))
    aaa.remove(aa[k])
    sinnn.remove(sinn[k])
    for j in range(len(aaa)):
        a = []
        sin = []
        for i in range(len(aaa)):
            a.append(aaa[i])
            sin.append((sinnn[i]))
        a.remove(aaa[j])
        sin.remove(sinnn[j])

        g = (summ(a, sin) - sum(a) * sum(sin) / len(a)) / (summ(sin, sin) - sum(sin) ** 2 / len(a))
        B = g
        A = (sum(a) - B * sum(sin)) / len(a)
        D = summ(sin, sin) - sum(sin) ** 2 / len(a)
        d = []
        for p in range(len(a)):
            d.append(a[p] - (A + B * sin[p]))

        sigma = math.sqrt(summ(d, d) / (D * (len(a) - 2)))
        delta = sigma * 2
        print(g, A, B, delta, sigma)

plt.scatter(sinn, aa, color="red", s=75, label="Экспериментальные данные")
x_s = np.linspace(0, 0.1)
A = -0.08847077900503823
B = 9.404187070528977

# plt.plot(x_s, x_s * 0.071744375, color="green", linewidth=1.5, label="Y=aZ(а получен МНК)")

plt.plot(x_s, A + x_s * B, linewidth=3, label="a=A + Bsin(alpha); B = 9.4, A = -0.09")
plt.errorbar(sinn, aa, da, 0, label="Погрешности данных")
plt.legend(loc="upper left")
plt.grid(alpha=0.5)
plt.title('График зависимости a(ускорения) от sin(alpha)(угла наклона рельса)')
plt.ylabel('a, м/c^2')
plt.xlabel('sin(alpha)')
plt.show()
