import math

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from scipy.integrate import odeint


def dSdt(S, t, k):
    g = 9.82
    vx = S[0]
    vy = S[1]
    return [
        -k * vx,  # dvx/dt
        -k * vy - g  # dvy/dt
    ]


# const
g = 9.82
k = 0.0
dt = 0.0001  # шаг моделирования

# initial condition
x0 = 0
y0 = 0
v0 = 20  # стартовая скорость
alpha = 45  # cтартовый угол
v0x = v0 * math.cos(math.radians(alpha))
v0y = v0 * math.sin(math.radians(alpha))
t = np.linspace(0, 100, int(100 / dt))

while k < 2.3:
    sol = odeint(dSdt, [v0x, v0y], t, args=(k,))
    vx = sol.T[0]
    vy = sol.T[1]
    x = [0]
    y = [0]
    for i in range(len(vx)):
        x.append(x[len(x) - 1] + vx[i] * dt)
        y.append(y[len(y) - 1] + vy[i] * dt)
        if y[len(y) - 1] < 0:
            break
    plt.plot(x, y, label="k =" + str(k))
    print(k, max(x), max(y))
    k += 0.25

# оформление графика
plt.ylabel("y, м")
plt.xlabel("x, м")
plt.legend()
plt.title(
    "Сравнение траекторий при различных значениях сопротивления k,\nначальная скорость 20м/с, стартовый угол 45 градусов")
plt.grid()
plt.show()
