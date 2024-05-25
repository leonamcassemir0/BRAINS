import pandas as pd

"""
# Set up code checking
from learntools.core import binder
binder.bind(globals())

from learntools.machine_learning.ex2 import *
print("Setup complete")
"""

# Path of the file to read
iowa_file_path = 'melb_data.csv'

# Read the doc
home_data = pd.read_csv(iowa_file_path)

"""
Call in the line below with no argument to check that
you´ve loaded data correctly
"""
# home_data.check()

# Print the summary statistics in next line
print(home_data.describe())

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home
# (current year - the date in which it was built)
newest_home_age = 14
