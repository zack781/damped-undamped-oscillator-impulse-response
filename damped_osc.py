#damped_osc.py by Zack Nguyen
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define system parameters
m = 1.0       # Mass (kg)
k = 4.0       # Spring constant (N/m)
c = 0.5       # Damping coefficient (kg/s)

# Derived parameters
omega_n = np.sqrt(k/m)            # Natural angular frequency (rad/s)
beta = c / (2*m)                   # Damping factor (1/s)
omega_d = np.sqrt(omega_n**2 - beta**2)  # Damped angular frequency (rad/s)

# Initial conditions
x0 = 1.0      # Initial displacement (m)
v0 = 0.0      # Initial velocity (m/s)

# Time span for the simulation
t_start = 0.0
t_end = 10.0
num_points = 1000
t_eval = np.linspace(t_start, t_end, num_points)

# Define the ODE system
def damped_oscillator(t, y):
    """
    Defines the differential equations for a damped harmonic oscillator.

    Parameters:
    - t: Time variable
    - y: List containing [displacement, velocity]

    Returns:
    - dydt: List containing [velocity, acceleration]
    """
    x, v = y
    dxdt = v
    dvdt = -(c/m)*v - (k/m)*x
    return [dxdt, dvdt]

# Solve the ODE numerically using solve_ivp
solution = solve_ivp(damped_oscillator, [t_start, t_end], [x0, v0], t_eval=t_eval, method='RK45')

# Extract numerical solution
t_num = solution.t
x_num = solution.y[0]

# Analytical solution
A = x0
B = (v0 + beta * x0) / omega_d
x_analytical = np.exp(-beta * t_num) * (A * np.cos(omega_d * t_num) + B * np.sin(omega_d * t_num))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t_num, x_num, label='Numerical Solution (RK45)', linewidth=2)
plt.plot(t_num, x_analytical, '--', label='Analytical Solution', linewidth=2)
plt.title('Damped Harmonic Oscillator: Numerical vs Analytical Solution', fontsize=14)
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Displacement (m)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

