import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
from statistics import NormalDist

# Generate some data for this
# demonstration.
data = [
    1.51,
    1.58,
    1.58,
    1.6,
    1.6,
    1.6,
    1.61,
    1.61,
    1.61,
    1.62,
    1.62,
    1.62,
    1.63,
    1.63,
    1.64,
    1.64,
    1.64,
    1.64,
    1.65,
    1.66,
    1.66,
    1.66,
    1.66,
    1.66,
    1.66,
    1.67,
    1.68,
    1.68,
    1.68,
    1.68,
    1.69,
    1.69,
    1.7,
    1.7,
    1.7,
    1.71,
    1.71,
    1.71,
    1.72,
    1.72,
    1.73,
    1.73,
    1.73,
    1.74,
    1.75,
    1.77,
    1.78,
    1.8,
    1.8,
    1.81

]
a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
for q in data:
    if 1.5529 > q >= 1.51:
        a += 1
    elif 1.5529 <= q < 1.5957:
        b += 1
    elif 1.5957 <= q < 1.6386:
        c += 1
    elif 1.6386 <= q < 1.6814:
        d += 1
    elif 1.6814 <= q < 1.7243:
        e += 1
    elif 1.7243 <= q < 1.7671:
        f += 1
    else:
        g += 1
print(a, b, c, d, e, f, g)
# Fit a normal distribution to
# the data:
# mean and standard deviation
mu, std = norm.fit(data)

# Plot the histogram.
bins_list = [1.53,
             1.57,
             1.62,
             1.66,
             1.70,
             1.75,
             1.79]

plt.hist(data, bins=7, density=True, alpha=0.6, color='b', label='Гистограмма dN/(Ndt)')
# (n, bins, patches) = plt.hist(data, bins_list, density=True, alpha=0.6, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

# mu-average std-dispercion
plt.plot(x, p, '-r', linewidth=2, label="Функция Гаусса")
title = "<t> = {:.2f}; sigma = {:.2f}".format(mu, std)
plt.title('График плотности вероятности от времени')
plt.xlabel('t, c')

plt.ylabel('Распределение плотности вероятности по t, c^-1')
c, cc, ccc = 0, 0, 0
for i in data:
    if mu - std <= i <= mu + std:
        c += 1
    if mu - 2 * std <= i <= mu + 2 * std:
        cc += 1
    if mu - 3 * std <= i <= mu + 3 * std:
        ccc += 1


# print(c, c / len(data), mu - std, mu + std)
##print(cc, cc / len(data), mu - 2 * std, mu + 2 * std)
# print(ccc, ccc / len(data), mu - 3 * std, mu + 3 * std)


def normpdf(x, mean, sd):
    var = float(sd) ** 2
    denom = (2 * math.pi * var) ** .5
    num = math.exp(-(float(x) - float(mean)) ** 2 / (2 * var))
    return num / denom


dots = []
for d in bins_list:
    dots.append(normpdf(d, 1.67, 0.062812))

plt.scatter(bins_list, dots, c="b", s=50, label="Toчки р(t)")
plt.legend(loc="upper left")
plt.show()
