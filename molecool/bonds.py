"""
bonds.py
Analyzing and Visualizing Molecules (MOLSSI)

Handles the primary functions
"""
    
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

atom_colors = {
    'H': 'white',
    'C': '#D3D3D3',
    'N': '#add8e6',
    'O': 'red',
    'P': '#FFA500',
    'F': '#FFFFE0',
    'Cl': '#98FB98',
    'Br': '#F4A460',
    'S': 'yellow'
}