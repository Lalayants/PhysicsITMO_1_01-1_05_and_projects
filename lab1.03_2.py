import math
import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

a = [0.270384615,
     0.381230769,
     0.536,
     0.654769231,
     0.764846154,
     0.901923077,
     1.030153846]

t = [17.18930769,
     24.5408,
     32.494,
     39.41049231,
     46.18128462,
     53.50846154,
     59.77095385]

V = 0
N = 0
am = sum(a) / len(a)  # x
tm = sum(t) / len(t)  # y
plt.scatter(a, t, color="red", s=75, label="Экспериментальные данные")
for i in range(len(a)):
    V += (a[i] - am) * (t[i] - tm)
    N += (a[i] - am) ** 2
m = V / N
f = tm - am * m
x = np.linspace(0, max(a))
plt.plot(x, x * m + f, color="blue", label="T = Fтр + a * М1(легкая)")
plt.legend(loc="upper left")
plt.grid(alpha=0.5)
plt.title('График зависимости T=T(a)')
plt.ylabel('T, мH')
plt.xlabel('a, м/c^2')

print('Ftr = ' + str(f) + '   M1 = ' + str(m))
d = []
D = 0
Dyy = 0
Dxx = 0
dsq = 0
xx = 0
yy = 0
xy = 0
for i in range(len(a)):
    d.append(t[i] - (f + m * a[i]))
    D += (a[i] - am) ** 2
    dsq += (t[i] - (f + m * a[i])) ** 2
    xy += t[i] * a[i]
    xx += a[i] ** 2
    yy += t[i] ** 2

Sb = dsq / (D * (len(a) - 2))
Sa = (1 / len(a) + am ** 2 / D) * dsq / (len(a) - 2)
x = 1
delta = math.sqrt(4 * Sa ** 2 + Sb * x ** 2)
sigma = math.sqrt((yy / xx - m ** 2) / (len(a) - 2))
print('sigma = ' + str(sigma))

a = [
    0.13,
    0.20,
    0.27,
    0.34,
    0.39,
    0.47,
    0.53
]

t = [17.44,
     25.01,
     33.42,
     40.77,
     48.07,
     56.13,
     63.17]
V = 0
N = 0
am = sum(a) / len(a)  # x
tm = sum(t) / len(t)  # y

for i in range(len(a)):
    V += (a[i] - am) * (t[i] - tm)
    N += (a[i] - am) ** 2
m = V / N
f = tm - am * m
x = np.linspace(0, max(a))
plt.plot(x, x * m + f, label="T = Fтр + a * М2(тяжелая)")
plt.scatter(a, t, s=75, color="orange", label="Экспериментальные данные")
plt.legend(loc="upper left")
plt.grid(alpha=0.5)
plt.title('График зависимости T=T(a)')
plt.ylabel('T, мH')
plt.xlabel('a, м/c^2')

print('Ftr = ' + str(f) + '   M1 = ' + str(m))
d = []
D = 0
Dyy = 0
Dxx = 0
dsq = 0
xx = 0
yy = 0
xy = 0
for i in range(len(a)):
    d.append(t[i] - (f + m * a[i]))
    D += (a[i] - am) ** 2
    dsq += (t[i] - (f + m * a[i])) ** 2
    xy += t[i] * a[i]
    xx += a[i] ** 2
    yy += t[i] ** 2

Sb = dsq / (D * (len(a) - 2))
Sa = (1 / len(a) + am ** 2 / D) * dsq / (len(a) - 2)
x = 1
delta = math.sqrt(4 * Sa ** 2 + Sb * x ** 2)
sigma = math.sqrt((yy / xx - m ** 2) / (len(a) - 2))
print('sigma = ' + str(sigma))
plt.show()
