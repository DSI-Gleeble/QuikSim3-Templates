# Thermal Reheat Cycle

A Table program that heats a specimen from ambient to 900 °C over 60 seconds,
holds for 30 seconds, and then cools back to ambient over 45 seconds. No
mechanical deformation is applied — the test is pure thermal.

## What it demonstrates

- Thermal-only Table programs (no stroke or wedge motion)
- Controlled heating, soaking, and cooling segments
- Dual TC acquisition for temperature gradient checks

## Segments

| # | Time      | TC1 target |
|---|-----------|------------|
| 1 | 01:00.0   | 900 °C     |
| 2 | 00:30.0   | 900 °C     |
| 3 | 00:45.0   | 25 °C      |

## How to use

Open in QuikSim3 and save a copy via **File → Save As** before running.
Adjust the temperatures or durations to match your material's processing
window.
