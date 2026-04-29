# Ti-6Al-4V HAZ Simulation

A HAZ (Heat Affected Zone) program reproducing the thermal cycle a Ti-6Al-4V
specimen experiences in a butt weld, using the Rykalin 3-D analytical model
to compute cool-time from energy input and geometry.

## What it demonstrates

- Rykalin 3-D HAZ model configuration
- Titanium material properties (density, specific heat, thermal conductivity)
- Peak-temperature-driven weld thermal cycle
- Pre-weld soak to set the baseline temperature

## Key parameters

| Parameter            | Value     |
|----------------------|-----------|
| Peak weld temp       | 1200 °C   |
| Pre-weld temp        | 400 °C    |
| Energy input         | 15 kJ/mm  |
| Heat rate            | 500 °C/s  |
| Hold time at peak    | 0.01 s    |
| Cool time (0.8→0.5)  | 19.8 s    |
| Weld speed           | 1 mm/s    |
| Distance from weld   | 0.5 mm    |

## Material constants

| Property        | Value      |
|-----------------|------------|
| Density         | 4.43 g/cm³ |
| Specific heat   | 0.526 J/g·K |
| Thermal cond.   | 0.067 W/mm·K |

## How to use

Open in QuikSim3 and use **File → Save As** to place a working copy in your
project. Adjust the energy input, peak temperature, or distance-from-weld to
match your experimental conditions.
