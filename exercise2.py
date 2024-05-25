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

# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)
y = home_data.SalePrice