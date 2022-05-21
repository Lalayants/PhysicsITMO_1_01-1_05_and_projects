import matplotlib.pyplot as plt
import math
import numpy as np


def getTrajectory(v, alp):
    v_st_x = v * math.cos(math.radians(alp))
    v_st_y = v * math.sin(math.radians(alp))
    tr_x = [0]
    tr_y = [0]
    delta_t = 0.001
    while tr_y[-1] >= 0:
        v_st_y -= 9.8 * dt
        tr_x.append((tr_x[-1] + v_st_x * delta_t))
        tr_y.append((tr_y[-1] + v_st_y * delta_t))
    return [tr_x, tr_y]


# стартовые параметры
alpha = 45
v_start = 10
dt = 0.001
d_alpha = 10
plt.title("График зоны поражения снаряда при cтартовой скорости = " + str(v_start) + "м/с")

# перебор углов
while alpha <= 90:
    a = getTrajectory(10, alpha)
    print(alpha, max(a[0]), max(a[1]))
    plt.fill_between(a[0], a[1], np.zeros_like(a[1]), label=alpha, alpha=0.5)
    alpha += d_alpha
# оформление графика
plt.grid()
plt.xlabel("x, м")
plt.ylabel("y, м")
plt.show()

# график 20 - 45
a = getTrajectory(20, 45)
print(45, max(a[0]), max(a[1]))
plt.plot(a[0], a[1])
print(max(a[0]), max(a[1]))

# оформление графика
plt.title("График зоны поражения снаряда при cтартовой скорости = " + str(20) + "м/с, \n cтартовом угле 45 градусов")
plt.grid()
plt.xlabel("x, м")
plt.ylabel("y, м")
plt.show()
