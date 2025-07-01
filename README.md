# ISC-Visualization

**Dynamic In-Situ Combustion Front Simulation**
This Python code simulates the temperature, viscosity, and zone profiles of a combustion front propagating through a core sample during an in-situ combustion (ISC) process, commonly studied in thermal Enhanced Oil Recovery (EOR).

**Features**<br>

**Dynamic Temperature Profile**: Models how temperature evolves along the core as the combustion front advances over time.

**Viscosity Calculation**: Computes oil viscosity as a function of temperature using an Arrhenius-type relation.

**Zone Classification**: Classifies the reservoir into zones (Initial Reservoir, Oil Bank, Condensation Zone, Steam Zone, Combustion Zone, Burned Zone) based on temperature and position relative to the front.

**Interactive Visualization**: Includes an interactive slider to view how profiles change with time.

**Plots Generated**:

Temperature vs. Distance
Viscosity vs. Distance (log scale)
Zone heatmap along the core

**Technologies Used**

numpy for numerical operations
matplotlib for plotting and visualization
ipywidgets for interactive slider control in Jupyter Notebooks
