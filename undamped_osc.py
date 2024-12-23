#undamped_osc.py by Zack Nguyen
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the undamped oscillator
A = 1.0            # Amplitude (meters)
omega_n = 2 * np.pi  # Natural angular frequency (rad/s), e.g., 1 Hz
phi = 0            # Phase angle (radians)

# Time settings
t_start = 0        # Start time (seconds)
t_end = 5          # End time (seconds)
num_points = 1000  # Number of points in time array

# Create a time array
t = np.linspace(t_start, t_end, num_points)

# Analytical solution for displacement x(t)
x = A * np.cos(omega_n * t + phi)

# Plotting the undamped oscillator motion
plt.figure(figsize=(10, 6))
plt.plot(t, x, label=r'$x(t) = A \cos(\omega_n t + \phi)$', color='blue')
plt.title('Undamped Harmonic Oscillator')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

