import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file = 'melb_data.csv'
melb_read = pd.read_csv(melbourne_file)

# columns show the comlumns in the dataset.
# print(melb_read.columns)

# By convention, the prediction target is called y.
y = melb_read.Price

# Features
melbourne_features = [
    'Rooms', 'Bathroom', 'Landsize', 'Lattitude',
    'Longtitude']
x = melb_read[melbourne_features]
# print(x.describe())
# head() method returns first five lines of the Dataframe.
# print(x.head())
# By convention, this data is called x.


# Buildind Your Model

# Define model.
# Specify a number for random_state to ensure same results each run.
melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
melbourne_model.fit(x, y)
# Specifying a number for random_state ensures you get the same results in each run. 
# This is considered a good practice.
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))