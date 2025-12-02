import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A = sp.Matrix([
    [-3, -6, -10, 10],
    [1, -1, 0, 0],
    [0, 1, -2, 3],
    [0, 0, 1, -2]
    ])

B = sp.Matrix([[1], [0], [0], [0]])
C = sp.Matrix([[1, -4, -2, 10]])
D = sp.Matrix([[0]])

s = sp.symbols('s')
I = sp.eye(4)

G_s = sp.simplify(C * (s*I - A).inv() * B + D)
G_s = sp.simplify(G_s[0])

num, den = sp.fraction(sp.simplify(G_s))

print("Part 1")
print('G(s) = ', G_s)
print('Numerator =', sp.factor(num))
print("Denominator =", sp.factor(den))

g = sp.gcd(num, den)
num_r = sp.simplify(num/g)
den_r = sp.simplify(den/g)
mcmillan_deg = sp.degree(den_r, s)

print("GCD(num, den) = ", g)
print('McMillan degree = ', mcmillan_deg)

#Part 2 
n = 4

cont = B

for i in range(1, n):
    cont = cont.row_join(A**i * B)

obs = C
for i in range(1, n):
    obs = obs.col_join(C * A**i)

rank_cont = cont.rank()
rank_obs = obs.rank()

print("\nPart 2")
print('Controllability rank = ', rank_cont)
print('Observability rank = ', rank_obs)

if rank_cont == n and rank_obs == n:
    print("System is minimal")
else:
    print("System is not minimal")

A_min, B_min, C_min, D_min = A, B, C, D

# Part 3

u0 = 30

G0 = sp.simplify(G_s.subs(s, 0))
y_inf = u0  * G0

print("\nPart 3")
print('G(0) = ', G0)
print('y_infinity = ', float(y_inf))

A_np = np.array(A, dtype = float)
B_np = np.array(B, dtype = float)
C_np = np.array(C, dtype = float)
D_np = np.array(D, dtype = float)

t_end = 10

N = 2001
t_vals = np.linspace(0, t_end, N)
dt = t_vals[1] - t_vals[0]

x = np.zeros((4, 1))
y_vals = np.zeros(N)

for i, t in enumerate(t_vals):
    y_vals[i] = float(C_np @ x + D_np * u0)
    xdot = A_np @ x + B_np * u0
    x = x + xdot * dt

plt.figure(figsize=(10, 10))
plt.plot(t_vals, y_vals, label = 'y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.axhline(float(y_inf), color = 'r', label = 'y_infinity')
plt.title('Response to u(t) = 30 * 1(t)')
plt.grid(True)
plt.legend()
plt.show()