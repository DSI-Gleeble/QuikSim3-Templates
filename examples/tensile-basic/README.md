# Basic Tensile Test

A beginner-friendly HDS program that ramps a specimen to 1000 °C, soaks for
30 seconds, and then pulls it in tension to 50% engineering strain at a strain
rate of 1 s⁻¹.

## What it demonstrates

- Single-hit stroke-controlled tensile deformation
- Temperature soak before deformation
- Heat-mute during deformation to prevent power feedback artefacts
- Controlled cooldown after the hit

## Key parameters

| Parameter        | Value      |
|------------------|------------|
| Peak temperature | 1000 °C    |
| Ramp rate        | 10 °C/s    |
| Soak time        | 30 s       |
| Strain           | 0.5 (eng)  |
| Strain rate      | 1 s⁻¹      |
| Acquisition rate | 1000 Hz    |

## How to use

Open the example in QuikSim3, then use **File → Save As** to save a copy into
your own project before running. The example itself is read-only.
