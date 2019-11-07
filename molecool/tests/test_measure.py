"""
Unit Testing for Measure Module.
"""

import numpy as np
import molecool
import pytest

def test_calculate_distance():
    
    Atom_A = np.array([0.0, 0.0, 0.0])
    Atom_B = np.array([1.0, 0.0, 0.0])

    expected_distance = 1.0

    calculated_distance = molecool.calculate_distance(Atom_A, Atom_B)

    assert expected_distance == calculated_distance

def test_calculate_angle():

    rA = np.array([0.0, 0.0, -1.0])
    rB = np.array([0.0, 0.0, 0.0])
    rC = np.array([1.0, 0.0, 0.0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(rA, rB, rC, degrees=True)

    assert expected_angle == calculated_angle

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
    (np.array([np.sqrt(3)/2, 1/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30)
    ])
def test_calculated_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert calculated_angle == expected_angle

