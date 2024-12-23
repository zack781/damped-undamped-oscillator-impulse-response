import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
m = 1.0       # mass (kg)
k = 1.0       # spring constant (N/m)
c = 0.2       # damping coefficient (kg/s) - set to 0 for undamped
F0 = 1.0      # impulse magnitude (N)
omega = 1.5   # driving frequency (rad/s)

# Time settings
t_start = 0
t_end = 20
dt = 0.01
t_eval = np.arange(t_start, t_end, dt)

# Analytical Solution for Undamped Oscillator
def analytical_undamped(t):
    return (F0/m) * np.sin(omega * t) * (1 - np.cos(omega * t))

# Analytical Solution for Damped Oscillator
def analytical_damped(t):
    gamma = c / (2 * m)
    omega0 = np.sqrt(k / m)
    omega_d = np.sqrt(omega0**2 - gamma**2)
    return (F0/m / omega_d) * np.exp(-gamma * t) * np.sin(omega_d * t)

# Numerical Solution
def oscillator(t, y):
    x, v = y
    dxdt = v
    dvdt = (F0 * np.sin(omega * t) - c * v - k * x) / m
    return [dxdt, dvdt]

# Initial conditions
y0 = [0, 0]

# Solve ODE
sol = solve_ivp(oscillator, [t_start, t_end], y0, t_eval=t_eval, method='RK45')
t = sol.t
x_num = sol.y[0]

# Choose appropriate analytical solution
if c == 0:
    x_ana = analytical_undamped(t)
else:
    x_ana = analytical_damped(t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x_num, label='Numerical Solution', linestyle='--')
plt.plot(t, x_ana, label='Analytical Solution', alpha=0.7)
plt.title('Impulse Response: Numerical vs. Analytical Solutions')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.grid(True)
plt.show()
