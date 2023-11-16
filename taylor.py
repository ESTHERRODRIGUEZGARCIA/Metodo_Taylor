import matplotlib.pyplot as plt

def euler(f, x0, y0, h, num_steps):
    u = []
    v = []
    for i in range(num_steps):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        u.append(x0)
        v.append(y0)
    return u, v

def taylor_second_order(f, df_dy, x0, y0, h, num_steps):
    u = []
    v = []
    for i in range(num_steps):
        # Método de Euler para obtener y_{i+1}
        y0 = y0 + h * f(x0, y0)

        # Método de Taylor de segundo orden para obtener y_{i+1}
        y0 = y0 + h * (f(x0, y0) + 0.5 * h * df_dy(x0, y0))

        x0 = x0 + h
        u.append(x0)
        v.append(y0)
    return u, v

def f(x, y):
    return (1 + 4*x*y) / (3*x*x)

def df_dy(x, y):
    return 4 / (3 * x)

# Definir la región R
x_min, x_max = 0.5, 4.0
y_min, y_max = -3.0, 3.0

# Condiciones iniciales
x0 = 0.5
y0 = -1
h = 0.035
num_steps = 100

# Solución utilizando el método de Euler
u_euler, v_euler = euler(f, x0, y0, h, num_steps)

# Solución utilizando el método de Taylor de segundo orden
u_taylor, v_taylor = taylor_second_order(f, df_dy, x0, y0, h, num_steps)

# Graficar ambas soluciones
plt.plot(u_euler, v_euler, label='Solución Real (Euler)')
plt.plot(u_taylor, v_taylor, label='Solución Numérica (Taylor 2º orden)')

# Líneas verticales que representan los límites de la región R
plt.axvline(x=x_min, color='r', linestyle='--', label='Límite inferior de x')
plt.axvline(x=x_max, color='r', linestyle='--', label='Límite superior de x')

# Líneas horizontales que representan los límites de la región R
plt.axhline(y=y_min, color='g', linestyle='--', label='Límite inferior de y')
plt.axhline(y=y_max, color='g', linestyle='--', label='Límite superior de y')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparación entre Solución Real y Solución Numérica')
plt.grid(True)
plt.show()

# Imprimir el valor de w_100 para ambas soluciones
print(f"El valor aproximado de w_100 (Euler) es {v_euler[-1]}")
print(f"El valor aproximado de w_100 (Taylor 2º orden) es {v_taylor[-1]}")
