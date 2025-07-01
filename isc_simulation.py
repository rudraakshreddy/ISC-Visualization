import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from ipywidgets import interact, IntSlider

# ==== USER INPUT SECTION ====
core_length_cm = 300
dx_cm = 1.0     # step size for distance
T_initial_C = 60
T_max_C = 600  # Max temperature at the combustion front
# ============================

# Derived
x_vals = np.arange(0, core_length_cm + dx_cm, dx_cm)
n_points = len(x_vals)

# Temperature profile function
def temperature_profile_dynamic(x, front_x, T_initial, T_max):
    if x <= front_x:
        return T_initial + (T_max - T_initial) * (x / front_x)**2 if front_x != 0 else T_initial
    else:
        return T_initial + (T_max - T_initial) * np.exp(-(x - front_x) / 30)

# Viscosity model
def calculate_viscosity(T_vals):
    A_mu = 0.002
    B_mu = 1800
    return A_mu * np.exp(B_mu / (T_vals + 273.15))

# Zone classification with delayed development
def classify_zones_dynamic(x_vals, T_vals, front_x):
    zones = np.zeros_like(T_vals, dtype=int)
    if front_x < 30:  # Delay zone development until front has moved 30 cm
        return zones  # Only initial reservoir

    for i, (x, T) in enumerate(zip(x_vals, T_vals)):
        if x < front_x - 20:
            zones[i] = 5  # Burned Zone
        elif front_x - 20 <= x < front_x:
            zones[i] = 4  # Combustion Zone
        elif front_x <= x < front_x + 20 and T > 350:
            zones[i] = 3  # Steam Zone
        elif 200 < T <= 350:
            zones[i] = 2  # Condensation Zone
        elif 80 < T <= 200:
            zones[i] = 1  # Oil Bank
        else:
            zones[i] = 0  # Initial Reservoir
    return zones

# Plotting function
def plot_all_dynamic(time_min):
    front_velocity_cm_per_min = 0.5  # Define front velocity
    front_x = front_velocity_cm_per_min * time_min

    T_vals = np.array([temperature_profile_dynamic(x, front_x, T_initial_C, T_max_C) for x in x_vals])
    mu_vals = calculate_viscosity(T_vals)
    zones = classify_zones_dynamic(x_vals, T_vals, front_x)

    zone_labels = {
        0: "Initial Reservoir",
        1: "Oil Bank",
        2: "Condensation Zone",
        3: "Steam Zone",
        4: "Combustion Zone",
        5: "Burned Zone"
    }
    zone_colors = {
        0: '#a6cee3',
        1: '#b2df8a',
        2: '#ffbb78',
        3: '#1f78b4',
        4: '#fb9a99',
        5: '#999999'
    }

    # Temperature plot
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, T_vals, 'r-', linewidth=2)
    plt.axvline(front_x, color='k', linestyle='--', label='Combustion Front')
    plt.title(f"Temperature Profile at {time_min} min")
    plt.xlabel("Distance (cm)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Viscosity plot
    plt.figure(figsize=(8, 5))
    plt.semilogy(x_vals, mu_vals, 'b-', linewidth=2)
    plt.axvline(front_x, color='k', linestyle='--', label='Combustion Front')
    plt.title(f"Viscosity Profile at {time_min} min")
    plt.xlabel("Distance (cm)")
    plt.ylabel("Viscosity (cP)")
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Zone Heatmap
    plt.figure(figsize=(8, 2))
    cmap = mcolors.ListedColormap([zone_colors[z] for z in sorted(zone_colors)])
    zone_map = zones.reshape(1, -1)
    plt.imshow(zone_map, cmap=cmap, aspect='auto', extent=[x_vals.min(), x_vals.max(), 0, 1])
    plt.yticks([])
    plt.xlabel("Distance (cm)")
    plt.title(f"Zone Heatmap at {time_min} min")
    legend_patches = [mpatches.Patch(color=zone_colors[z], label=zone_labels[z]) for z in sorted(zone_labels)]
    plt.legend(handles=legend_patches, bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Interactive slider for time
interact(plot_all_dynamic, time_min=IntSlider(value=0, min=0, max=500, step=10, description='Time (min)'))