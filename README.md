# Critical State Properties of Fluids Using Cantera

This repository contains Python code that calculates and prints the critical state properties of various fluids using Cantera's built-in liquid/vapor equations of state.

## Overview

The critical state properties, including critical temperature, critical pressure, and compressibility factor, are vital for understanding the thermodynamic behavior of fluids in various engineering applications. This project provides a simple and effective way to access these properties for several common fluids.

## Features

- **Fluids Supported**: Calculates critical properties for multiple fluids, including water, nitrogen, methane, hydrogen, oxygen, carbon dioxide, heptane, and HFC-134a.
- **Easy to Use**: Just run the script to get the critical state properties for the selected fluids.

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
                Fluid  Tc [K]      Pc [Pa]          Zc
                water    647.1      22.06e6      0.2244
             nitrogen     126.2       33.5e5      0.1848
              methane     190.6       46.0e5      0.2516
             hydrogen      33.2       12.8e5      0.2435
                oxygen     154.6       50.4e5      0.2415
        carbon dioxide     304.2       73.8e5      0.2630
              heptane     540.0      18.5e6      0.2917
               hfc134a     374.2       40.5e5      0.2351
```

## Acknowledgments

- **Cantera**: A powerful tool for chemical thermodynamics, which provides the functionality to calculate the properties used in this project.
- **Numerical Methods for Engineers**: The foundational text that inspired the use of thermodynamic principles in this project.
