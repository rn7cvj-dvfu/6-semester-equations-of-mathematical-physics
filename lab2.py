import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    return np.sin(np.pi * x / 4) ** 2


def y_k(x, k):
    return np.cos(np.pi * k * x / 2)


def compute_c_k(k):
    result1, _ = quad(lambda x: f(x) * y_k(x, k), 0, 2)
    result2, _ = quad(lambda x: y_k(x, k) ** 2, 0, 2)
    result = result1 / result2
    return result


def parseval_check(N):
    integral_f2, _ = quad(lambda x: f(x) ** 2, 0, 2)
    sum_coeffs = sum(compute_c_k(k) ** 2 for k in range(N))
    print(f"Интеграл от f^2(x): {integral_f2:.6f}")
    print(f"Сумма квадратов коэффициентов Фурье: {sum_coeffs:.6f}")
    print(f"Разница: {abs(integral_f2 - sum_coeffs):.6f}")


x_vals = np.linspace(0, 2, 400)
y_true = f(x_vals)

N = 5
a_c_vals = [compute_c_k(k) for k in range(N)]


def fourier_series(x, N):
    return sum(compute_c_k(k) * y_k(x, k) for k in range(N))


y_fourier = [fourier_series(x, N) for x in x_vals]


parseval_check(N)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_true, label="Исходная функция", linewidth=2, color="black")
plt.plot(
    x_vals,
    y_fourier,
    label=f"Сумма первых {N} гармоник",
    linewidth=2,
    linestyle="--",
    color="red",
)


plt.xlabel("x")
plt.legend()
plt.title("Разложение в ряд Фурье")
plt.grid()
plt.show()
