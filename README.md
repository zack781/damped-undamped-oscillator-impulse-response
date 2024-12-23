# Harmonic Oscillator Simulations

This repository contains Python scripts for simulating and analyzing the motion of harmonic oscillators under different conditions. These include undamped oscillators, damped oscillators, and systems driven by external forces. The simulations use numerical and analytical methods to compare the results.

## Contents

### Files

1. **`undamped_osc.py`**
   - Simulates an undamped harmonic oscillator.
   - Uses analytical solutions to plot displacement as a function of time.
   - Dependencies: `numpy`, `matplotlib`.

2. **`damped_osc.py`**
   - Simulates a damped harmonic oscillator.
   - Compares numerical solutions (using `scipy.integrate.solve_ivp`) with analytical solutions.
   - Dependencies: `numpy`, `matplotlib`, `scipy`.

3. **`spring.py`**
   - Simulates a spring system with options for damping and external forcing.
   - Includes both numerical and analytical solutions.
   - Dependencies: `numpy`, `matplotlib`, `scipy`.

4. **`requirements.py`**
   - Lists the required Python libraries for running the simulations.
   - Use the following command to install the dependencies:
     ```bash
     pip install -r requirements.py
     ```

### Features

- **Numerical Simulations**: All scripts use `scipy.integrate.solve_ivp` for solving differential equations.
- **Analytical Solutions**: Wherever possible, analytical solutions are provided for comparison.
- **Visualization**: Plots of displacement over time are generated to illustrate the system behavior.

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the repository folder:
   ```bash
   cd <repository_folder>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.py
   ```

## Usage

- Run any of the scripts to visualize the behavior of the respective oscillator.
  Example:
  ```bash
  python undamped_osc.py
  ```

## Description of Parameters

### `undamped_osc.py`
- `A`: Amplitude of the oscillation.
- `omega_n`: Natural angular frequency.
- `phi`: Phase angle.
- `t_start`, `t_end`, `num_points`: Time settings for simulation.

### `damped_osc.py`
- `m`: Mass of the oscillator.
- `k`: Spring constant.
- `c`: Damping coefficient.
- `x0`, `v0`: Initial displacement and velocity.

### `spring.py`
- `m`: Mass of the oscillator.
- `k`: Spring constant.
- `c`: Damping coefficient.
- `F0`: Magnitude of the external force.
- `omega`: Driving frequency.

## Author

Zack Nguyen

## Dependencies

- `numpy` for numerical operations.
- `matplotlib` for plotting.
- `scipy` for solving differential equations.

