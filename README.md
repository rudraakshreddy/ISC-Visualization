# ISC-Visualization

**Dynamic In-Situ Combustion Front Simulation**<br>
This Python code simulates the temperature, viscosity, and zone profiles of a combustion front propagating through a core sample during an in-situ combustion (ISC) process, commonly studied in thermal Enhanced Oil Recovery (EOR).<br>
**Features**<br>

**Dynamic Temperature Profile**: Models how temperature evolves along the core as the combustion front advances over time.<br>

**Viscosity Calculation**: Computes oil viscosity as a function of temperature using an Arrhenius-type relation.<br>

**Zone Classification**: Classifies the reservoir into zones (Initial Reservoir, Oil Bank, Condensation Zone, Steam Zone, Combustion Zone, Burned Zone) based on temperature and position relative to the front.<br>

**Interactive Visualization**: Includes an interactive slider to view how profiles change with time.<br>

**Plots Generated**:
Temperature vs. Distance<br>
Viscosity vs. Distance (log scale)<br>
Zone heatmap along the core<br>

**Technologies Used**<br>
numpy for numerical operations<br>
matplotlib for plotting and visualization<br>
ipywidgets for interactive slider control in Jupyter Notebooks<br>
