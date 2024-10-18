# Critical State Properties of Fluids Using Cantera

This repository contains Python code that calculates and prints the critical state properties of various fluids using Cantera's built-in liquid/vapor equations of state.

## Overview

The critical state properties, including critical temperature, critical pressure, and compressibility factor, are vital for understanding the thermodynamic behavior of fluids in various engineering applications. This project provides a straightforward way to access these properties for several common fluids.

## Features

- **Fluids Supported**: Calculates critical properties for multiple fluids, including water, nitrogen, methane, hydrogen, oxygen, carbon dioxide, heptane, and HFC-134a.
- **Easy to Use**: Simply run the script to obtain the critical state properties for the selected fluids.

## Requirements

To run this code, you need:

- Python 3.x
- Cantera library installed

You can install Cantera using pip:

```bash
pip install cantera
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/iammohith/Critical-State-Properties-of-Fluids-Using-Cantera.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Critical-State-Properties-of-Fluids-Using-Cantera
   ```

3. Run the script:
   ```bash
   python critical_state_properties.py
   ```

## Example Output

Upon running the script, you will see output similar to the following:

```
Critical State Properties
               Fluid      Tc [K]     Pc [Pa]          Zc
               water        647.3    2.209E+07      0.2333
            nitrogen        126.2      3.4E+06      0.2891
             methane        190.6    4.599E+06      0.2904
            hydrogen        32.94    1.284E+06      0.3013
              oxygen        154.6    5.043E+06      0.2879
      carbon dioxide        304.2    7.384E+06      0.2769
             heptane        537.7     2.62E+06      0.2972
             hfc134a        374.2    4.059E+06        0.26
```

## Acknowledgments

- **Cantera**: A powerful tool for chemical thermodynamics, which provides the functionality to calculate the properties used in this project.
- **Numerical Methods for Engineers**: The foundational text that inspired the use of thermodynamic principles in this project.
