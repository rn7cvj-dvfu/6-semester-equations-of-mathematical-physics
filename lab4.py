import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

n = 20
t_grid = np.linspace(np.pi / 2, np.pi, 300)
f_exact = (
    -0.1
    * np.exp(-2 * t_grid)
    * (
        -3 * np.exp(3 * t_grid) * np.sin(t_grid)
        + np.exp(3 * t_grid) * np.cos(t_grid)
        + 3 * np.exp(3 * np.pi / 2)
        + 10 * np.exp(np.pi)
    )
)

t = sp.symbols("t")
s = sp.symbols("s")


def x_n(x):
    r = (
        sp.integrate(
            sp.exp(s) * sp.sin(s) - 2 * x,
            (s, np.pi / 2, t),
        )
        - 1
    )
    return r


t = sp.symbols("t")
x_i = 0

plt.figure(figsize=(10, 6))

for i in range(1, n + 1):
    x_i = x_n(x_i).subs(t, s)
    f = sp.lambdify(s, x_i, "numpy")(t_grid)
    print(f"{i}\t{np.max(np.abs(f - f_exact))}")
    plt.plot(t_grid, f, "--", label=f"$x_{{{i}}}(t)$")

plt.plot(
    t_grid,
    f_exact,
    label="Точное решение",
    linewidth=2,
)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)

# Вынесенная легенда снизу
plt.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=5,
    fontsize="large",
    frameon=True,
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.4)  # чтобы освободить место под легенду
plt.show()
