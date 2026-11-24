import matplotlib.pyplot as plt
import numpy as np


def taylor_ln(x, n):
  """Polinomio de Taylor de grado n de ln(x) alrededor de x0 = 1."""
  suma = 0
  for k in range(1, n + 1):
    suma = suma + (((-1) ** (k + 1)) * (x - 1) ** k) / k
  return suma


print(f"Verificacion: {taylor_ln(1.5, 3)}")
print(round(taylor_ln(1.5, 10), 6), round(taylor_ln(2.5, 10), 6))

# Grafica1
x = np.linspace(0.1, 3, 400)

plt.figure(figsize=(8, 5))
plt.plot(x, np.log(x), label=r"$\ln(x)$", linewidth=2)

for grado in [1, 2, 3, 6]:
  plt.plot(x, taylor_ln(x, grado), linestyle="--", label=rf"$P_{grado}(x)$")

plt.scatter([1], [0], color="red", zorder=5, label=r"Punto $(1, 0)$")
plt.ylim(-3, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Aproximación de Taylor de $\ln(x)$ en $x_0 = 1$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Grafica2
n_vals = np.arange(1, 31)

error_15 = np.array([np.abs(np.log(1.5) - taylor_ln(1.5, int(n))) for n in n_vals])
error_25 = np.array([np.abs(np.log(2.5) - taylor_ln(2.5, int(n))) for n in n_vals])
cota_15 = (0.5 ** (n_vals + 1)) / (n_vals + 1)

plt.figure(figsize=(8, 5))
plt.semilogy(n_vals, error_15, "o-", markersize=4, label=r"$|\ln(1.5) - P_n(1.5)|$")
plt.semilogy(n_vals, error_25, "s-", markersize=4, label=r"$|\ln(2.5) - P_n(2.5)|$")
plt.semilogy(n_vals, cota_15, "k--", label=r"Cota $\frac{0.5^{n+1}}{n+1}$ ($x=1.5$)")

plt.xlabel("Grado $n$")
plt.ylabel(r"Error $|\ln(x) - P_n(x)|$")
plt.title("Error de aproximación en escala logarítmica")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.show()