import math
import matplotlib.pyplot as plt
import math
import numpy as np

from sympy import *


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


dt = 0.001
g = 9.8
aim_x, aim_y = 30.0, 8
l = math.sqrt(aim_y ** 2 + aim_x ** 2)
V = math.sqrt(2 * l * g)
thetta1 = math.atan((V ** 2 - math.sqrt(V ** 4 - g * (g * aim_x ** 2 + 2 * V ** 2 * aim_y))) / (g * aim_x))
thetta2 = math.atan((V ** 2 + math.sqrt(V ** 4 - g * (g * aim_x ** 2 + 2 * V ** 2 * aim_y))) / (g * aim_x))
print("V = " + str(V))
print("Angels:" + str(thetta1) + " " + str(thetta2))
a = getTrajectory(V, math.degrees(thetta1))
plt.plot(a[0], a[1], alpha=0.5, label=str(int(math.degrees(thetta1) * 10) / 10) + "- угол запуска в градусах")
a = getTrajectory(V, math.degrees(thetta2))
plt.plot(a[0], a[1], alpha=0.5, label=str(int(math.degrees(thetta2) * 10) / 10) + "- угол запуска в градусах")
plt.scatter(aim_x, aim_y, color='r', label="target x = " + str(aim_x) + "м ,y = " + str(aim_y) + "м")
# оформление графика
plt.ylabel("y, м")
plt.xlabel("x, м")
plt.legend()
plt.title("Cтрельба в точку (" + str(aim_x) + " ," + str(aim_y) + ")." + "\nНачальная скорость = " + str(
    int(V * 10) / 10) + "м/c")
plt.grid()
plt.show()
