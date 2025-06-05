import sympy as sp

alpha = 0.25


def x_n(x):

    t = sp.symbols("t")
    s = sp.symbols("s")

    i = sp.E ** (t - s) * x

    r = alpha * sp.integrate(i, (s, 0, 1)) + 1
    r = r.subs(t, s)
    return r


s = sp.symbols("s")
t = sp.symbols("t")
x_0 = 1


x_1 = x_n(x_0)
x_2 = x_n(x_1)
x_3 = x_n(x_2)
x_4 = x_n(x_3)
x_5 = x_n(x_4)
x_6 = x_n(x_5)


sp.pretty_print(sp.expand(x_1.subs(s, t)))
print("__________________________")
sp.pretty_print(sp.expand(x_2.subs(s, t)))
print("__________________________")
sp.pretty_print(sp.expand(x_3.subs(s, t)))
print("__________________________")
sp.pretty_print(sp.expand(x_4.subs(s, t)))
print("__________________________")
sp.pretty_print(sp.expand(x_5.subs(s, t)))
print("__________________________")
sp.pretty_print(sp.expand(x_6.subs(s, t)))
