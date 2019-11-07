"""
molecool
Analyzing and Visualizing Molecules (MOLSSI)
"""

# From Functions.py Import Everything
# Necessary for Allowing Functions from Python Script
# import molecool.functions.canvas() Imports Canvas() Function Only
# Best Practice Tip: from molecool import canvas()
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
