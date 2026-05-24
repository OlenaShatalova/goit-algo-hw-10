import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Функція та межі інтегрування
def f(x):
    return x ** 2

a = 0
b = 2
N = 100000  # кількість випадкових точок

# --- Перевірка через quad ---
result, error = spi.quad(f, a, b)
print("Інтеграл (quad): ", result, error)

# --- Метод Монте-Карло ---
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = np.sum(y_random <= f(x_random))
rectangle_area = (b - a) * f(b)
monte_carlo_result = (under_curve / N) * rectangle_area

print(f"\nМетод Монте-Карло:    {monte_carlo_result:.6f}")
print(f"Функція quad (SciPy): {result:.6f}")
print(f"Похибка:              {abs(monte_carlo_result - result):.6f}")

# --- Графік ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()