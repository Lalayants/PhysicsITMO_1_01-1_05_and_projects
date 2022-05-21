import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

Y = [0.25,
     0.35,
     0.55,
     0.75,
     0.95]
Y_err = 0.007
Z = [3.525,
     4.5,
     7.125,
     10.88,
     13.3]
Z_err = [0.185254959,
         0.225459531,
         0.332278498,
         0.478086854,
         0.58094819]
Z_err = [0.465140361,
         0.501021179,
         0.586818162,
         0.683260159,
         0.750940151]
# linear_model = np.polyfit(Z, Y, 1)
# linear_model_fn = np.poly1d(linear_model)
# plt.plot(x_s, linear_model_fn(x_s), color="green", label="Y=aZ")
x_s = np.arange(0, 15)
plt.plot(x_s, x_s * 0.071744375, color="green", linewidth=1.5, label="Y=aZ(а получен МНК)")
plt.scatter(Z, Y, color="red", s=50, label="Экспериментальные данные")
plt.errorbar(Z, Y, Y_err, Z_err, label="Погрешности данных")

plt.legend(loc="upper left")
plt.grid(alpha=0.5)
plt.title('График зависимости Y(Перемещение тележки)\n от Z(Полу разность квадратов времени)')
plt.xlabel('Z, c^2')
plt.ylabel('Y, м')
plt.show()
