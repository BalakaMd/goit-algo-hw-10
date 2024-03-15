import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


a = 0
b = 2

n_points = 1000000
x_rand = np.random.uniform(a, b, n_points)
y_rand = np.random.uniform(0, f(b), n_points)

points_under_curve = sum(y_rand <= f(x_rand))
ratio = points_under_curve / n_points
rectangle_area = (b - a) * f(b)
integral_approximation = rectangle_area * ratio

print("Приблизне значення інтеграла методом Монте-Карло:", integral_approximation)

# Обчислення інтеграла за допомогою quad
result_quad = spi.quad(f, a, b)

print("Результат за допомогою quad:", result_quad)
