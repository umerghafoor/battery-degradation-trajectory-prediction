# Time-Series Data Analysis with Python

This repository contains Python scripts for reading, analyzing, and visualizing time-series data, specifically related to a battery or energy storage system. The code uses pandas for data manipulation, matplotlib for plotting, and includes various functions for data processing.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Variables](#variables)
4. [Contributing](#contributing)

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python (3.x recommended)
- Pandas
- Matplotlib

You can install the required dependencies using:

```
pip install pandas matplotlib pandas numpy
```
# Getting Started
1. Clone this repository:
```
git clone hhttps://github.com/umerghafoor/battery-degradation-trajectory-prediction
```
2. Install dependencies:
```
pip install pandas matplotlib pandas numpy
```
3. Download and palce data in data folder
    https://publications.rwth-aachen.de/record/818642
4. place in `data` folder
5. run `extract data.ipynb`

# Variables
- AhAkku: Total ampere-hours. With predominant discharge this value becomes negative [Ah]
- AhEla: Ampere-hours of all executed discharge steps until now [Ah]
- AhLad: Ampere-hours of all executed charge steps until now [Ah]
- AhStep: Ampere-hours of the current program step [Ah]
- Energie: Total energy. With predominant discharge this value becomes negative [Wh]
- Programmdauer: Time [ms]
- Prozedur: (secondary importance) Subprogram currently running.
- Prozedurebene: (secondary importance) Level of the subprogram depth currently running.
- Schritt: The program step that was executed when creating the registry entry [/]
- Schrittdauer: Time since the beginning of the step performed when creating the registry entry [ms]
- Spannung: Voltage [V]
- Strom: Current [A]
- TempX: cell surface temperature [°C]. Number X can be neglected and is cell specific.
- WhStep: Energy of the current program step [Wh]
- Zeit: Unix timestamp
- Zustand: State of the battery tester.
- Zyklus: In programs with loop constructions the Zyklus is an information about how many repetitions of the loop the registration entry was created.
- Zyklusebene: Can be neglected. (only non-zero when the test there is a loop within a loop)

# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.