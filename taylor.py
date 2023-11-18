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

def taylor(f, df_dx, df_dy, x, y, h, num_steps):
    
    u = []
    v = []
    for i in range(num_steps):
        y = y + h * f(x, y) + (h**2/2) * (df_dx(x, y) + df_dy(x, y) * f(x, y))
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    return (1 + 4*x*y)/(3*x**2)

def df_dx(x, y):
    return -(4*x*y + 2)/(3*x**3)

def df_dy(x, y):
    return (4)/(3*x)

def error(v, v_aprox):
    return abs(v - v_aprox)

# datos
x = 0.5
y = -1
h = 0.035
num_steps = 100

# Definir la región R
x_min, x_max = 0.5, 4.0
y_min, y_max = -3.0, 3.0

# Aplicamos el método de Taylor
u_taylor, v_taylor = taylor(f, df_dx, df_dy, x, y, h, num_steps)

# Imprimimos la última y del bucle
print('w_100 (Taylor): ', v_taylor[-1])

# Error
v_e = -11.46
error_taylor = error(v_e, v_taylor[-1])
print('Error (Taylor): ', error_taylor)

# Aplicamos el método de Euler para comparar
u_euler, v_euler = euler(f, x, y, h, num_steps)

# Imprimimos la última y del bucle
print('w_100 (Euler): ', v_euler[-1])

# Error
error_euler = error(v_e, v_euler[-1])
print('Error (Euler): ', error_euler)

# Graficar ambas soluciones
plt.plot(u_taylor, v_taylor, label='Solución Numérica (Taylor)')
plt.plot(u_euler, v_euler, label='Solución Numérica (Euler)')

# Líneas verticales que representan los límites de la región R
plt.axvline(x=x_min, color='r', linestyle='--', label='Límite inferior de x')
plt.axvline(x=x_max, color='r', linestyle='--', label='Límite superior de x')

# Líneas horizontales que representan los límites de la región R
plt.axhline(y=y_min, color='g', linestyle='--', label='Límite inferior de y')
plt.axhline(y=y_max, color='g', linestyle='--', label='Límite superior de y')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparación entre Solución Numérica (Euler y Taylor)')
plt.grid(True)
plt.show()
