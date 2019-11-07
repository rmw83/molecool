"""
measure.py
Analyzing and Visualizing Molecules (MOLSSI)

Handles the primary functions
"""
    
import numpy as np

def calculate_distance(Atom_A, Atom_B):
  
    """
    Distance Between Two Atoms.
    
    Parameters
    __________
    
    Atom_A, Atom_B : np.ndarray
        The Coordinates for Atom_A and Atom_B.
    
    Returns
    _______
    
    distance : float
        The Distance from Atom_A to Atom_B.
    
    Examples
    ________
    
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([1.0, 0.0, 0.0])
    >>> calculate_distance(r1, r2)
    1.0
    """

    difference = (Atom_A - Atom_B)
    distance = np.linalg.norm(difference)
    return distance
    
def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta