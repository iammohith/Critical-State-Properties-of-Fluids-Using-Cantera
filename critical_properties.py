#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:07:38 2020

@author: Mohith Sai
"""

"""
This script calculates and prints the critical state properties for various fluids
using Cantera's built-in liquid/vapor equations of state.
"""

import cantera as ct

# Define a dictionary of fluids with their respective Cantera classes
fluids = {
    'water': ct.Water(),
    'nitrogen': ct.Nitrogen(),
    'methane': ct.Methane(),
    'hydrogen': ct.Hydrogen(),
    'oxygen': ct.Oxygen(),
    'carbon dioxide': ct.CarbonDioxide(),
    'heptane': ct.Heptane(),
    'hfc134a': ct.Hfc134a()
}

# Print the header for the critical state properties table
print('Critical State Properties')
print('%20s  %10s  %10s  %10s' % ('Fluid', 'Tc [K]', 'Pc [Pa]', 'Zc'))

# Iterate through each fluid to calculate and display its critical properties
for name in fluids:
    f = fluids[name]  # Get the fluid object
    tc = f.critical_temperature  # Critical temperature [K]
    pc = f.critical_pressure  # Critical pressure [Pa]
    rc = f.critical_density  # Critical density [kg/m^3]
    mw = f.mean_molecular_weight  # Mean molecular weight [kg/kmol]
    
    # Calculate the compressibility factor at the critical point (Zc)
    zc = pc * mw / (rc * ct.gas_constant * tc)  # Compressibility factor
    
    # Print the properties in a formatted manner
    print('%20s   %10.4g   %10.4G  %10.4G' % (name, tc, pc, zc))
