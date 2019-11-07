"""
molecool
Analyzing and Visualizing Molecules (MOLSSI)
"""

# From Functions.py Import Everything
# Necessary for Allowing Functions from Python Script
# Import molecool.functions.canvas() Imports Canvas() Function Only
# Best Practice Tip: from molecool import canvas()

# If Starting from Starting Material...
# cookiecutter gh:molssi/cookiecutter-cms 
# pip install -e . 

from .measure import calculate_distance, calculate_angle
from .bonds import build_bond_list
from .draw import draw_molecule, bond_histogram
import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions