import math
import matplotlib.pyplot as plt
import numpy as np


def checkStop(omega___):
    if len(omega___) < 10:
        return True
    else:
        if abs(omega___[-1]) < 0.01 and abs(omega___[-3]) < 0.01:
            return False
        elif len(omega___) > 1000:
            return False
        return True


def dwdt(omega_, m_, g, k_, l_, t_, j_, angel_):
    abc = -m_ * g * l_ * math.sin(angel_) - k_ * l_ ** 2 * omega_
    cde = -math.copysign(1, omega_) * (m_ * g * abs(math.cos(angel_)) + m * omega_ ** 2 * l_) * k_2
    f = abc + cde
    # print(angel_, -math.atan2(k_2, 1) < angel_ < math.atan2(k_2, 1), -0.05 < omega_ < 0.05)
    if -math.atan2(k_2, 1) < angel_ < math.atan2(k_2, 1) and -0.05 < omega_ < 0.05:
        return 0
    return f / j_


def drawTrajectory(omega_start, angel_start, dt__, m__, g, k__, l__, j__):
    angel__ = [angel_start]
    omeg = [omega_start]
    t_now = [0]
    while checkStop(omeg):
        abc = angel__[-1] + omeg[-1] * dt__
        angel__.append(abc)
        omeg.append(omeg[-1] + dwdt(omeg[-1], m__, g, k__, l__, t_now[-1], j__, angel__[-1]) * dt)
        t_now.append(t_now[-1] + dt__)
        if omeg[-1] == omeg[-2]:
            for i in range(10):
                angel__.append(angel__[-1])
                t_now.append(t_now[-1] + dt__)
            break
    plt.plot(t_now, angel__, label="Отклонение маятника от положение 0")
    plt.plot(t_now, [0] * len(t_now), 'r--', label='положение 0')
    plt.title("График угла совершенных оборотов от времени\nphi(0) = " + str(phi_0)[0:5] + "рад w(0) = " + str(
        omega_0) + "рад/с\nk_стр = " + str(k_2) + " k_втр = " + str(k))
    plt.xlabel("Время t, c")
    plt.ylabel("Угол, рад")
    plt.legend()
    plt.grid()
    plt.show()
    # plt.plot(t_now, omeg, label="скорость угловая")
    # plt.legend()
    # plt.grid()
    # plt.show()
    return [t_now, angel__]


def getA(times, angels):
    y = [angels[0]]
    x = [0]
    for i in range(1, len(angels) - 1):

        print(angels[i - 1] < angels[i], angels[i] > angels[i + 1])
        if angels[i - 1] <= angels[i] and angels[i] >= angels[i + 1]:
            y.append(angels[i])
            x.append(times[i])
            print(y)
    plt.plot(x, y, label="Амплитуда")
    plt.plot(x, [0] * len(x), 'r--', label='положение 0')
    plt.title("График амплитуды от времени\nphi(0) = " + str(phi_0)[0:5] + "рад w(0) = " + str(
        omega_0) + "рад/с\nk_стр = " + str(k_2) + " k_втр = " + str(k))
    plt.xlabel("Время t, c")
    plt.ylabel("Амплитуда, рад")
    plt.legend()
    plt.grid()
    plt.show()


l = 1  # приведенная длина маятника
m = 1  # масса маятника
g = 9.82
k_2 = 0.1  # cухое трение
J_0 = 2 / 3 * l ** 2 * m  # момент инерции тела
phi_0 = math.pi * 1 / 6  # начальный угол отклонения
omega_0 = 1  # начальная скорость
k = 0.0  # трение о воздух
J = m * l ** 2 + J_0
dt = 0.1

plt.rcParams.update({'font.size': 9})
q, p = drawTrajectory(omega_0, phi_0, dt, m, g, k, l, J)
getA(q, p)

# def integrateAndPlot(dy, t_plot, c, dt_plot):
#     y = []
#     b = c
#     for i in range(len(dy)):
#         b += dy[i] * dt_plot
#         y.append(b)
#     plt.plot(t_plot, y)
#     plt.grid()
#     plt.show()
#
