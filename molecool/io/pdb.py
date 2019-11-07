"""
pdb.py
Analyzing and Visualizing Molecules (MOLSSI)

Handles the primary functions
"""

import numpy as np

def open_pdb(file_location):
    
    """
    Opens PDB File.
    
    Parameters
    __________
    
    file_location : str
        The Location for the PDB File.
    
    Returns
    _______
    
    symbols : list
        Gives Atomic Symbols for Atoms from PDB File.
    coordinates: np.ndarray
        Gives Atomic Coordinates for the PDB File.
    """
    
    # Reads PDB File and Returns Coordinates + Atom Names.
    with open(file_location) as pdb_file:
        pdb_data = pdb_file.readlines()
    pdb_file.close()
    
    # Generate Coordinates and Symbols Lists
    coordinates = []
    symbols = []
    
    # Cycle PDB_DATA 
    for line in pdb_data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)
    coordinates = np.array(coordinates)
    
    # End of Script
    return symbols, coordinates