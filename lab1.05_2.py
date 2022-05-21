import math
import matplotlib.pyplot as plt
import numpy as np

I = [0.0323, 0.0360, 0.0407, 0.0464, 0.0531, 0.0609]
T = [1.62, 1.71, 1.82, 1.94, 2.08, 2.22]
T = [x ** 2 for x in T]
x_sr = sum(I) / len(I)
y_sr = sum(T) / len(T)
b_u, b_d = 0, 0
for k in range(len(T)):
    b_u += (I[k] - x_sr) * (T[k] - y_sr)
    b_d += (I[k] - x_sr) ** 2
b = b_u / b_d
a = y_sr - b * x_sr
x = np.linspace(0.029, 0.063, 10)
print(*T)
# a = 0.0192
# b = 80.678
plt.plot(x, a + b * x, label="Аппроксимация y = ax+b, b = " + str(b)[0:6] + " a = " + str(-1 / b)[0:6])
plt.scatter(I, T, label="T^2(I) - экспериментальные данные")
plt.legend()
plt.grid()
plt.xlabel("I, кг*m^2")
plt.ylabel("T^2, c^2")
plt.title("График зависимости квадрата периода T^2 \n от момента инерции I")
plt.show()
print(4 * 3.14 ** 2 / (b * 9.82))
