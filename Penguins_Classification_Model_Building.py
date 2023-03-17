import streamlit as st
import pandas as pd

penguins = pd.read_csv('penguins_cleaned.csv')

df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix = col) 
    # The prefix parameter in the pd.get_dummies() method is used to add a prefix to 
    # the column name of each dummy variable created from a categorical column.
    # we applied pd.get_dummies() to the feature columns namely 'species' & 'Island' as 
    # they're are categorical features so we convert them into dummy variables (binary 0/1)
    df = pd.concat([df,dummy],axis=1) # the dummies created from categorical variable are concatenated horizonticaly (axis=1)
    del df[col]

target_mapper = {'Adelie':0,'Chinstrap':1,'Gentoo':2}
# target mapper is a dict that assigned unique value to each key that is species name
 
def target_encode(val):  
# target encode function is to return that unique value assigned to each
# unique species name 
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# so, basically what above code is doing is assigning a unique integer to each unique
# species column observation entry in the dataset 
# every 'Adelie' observation is labeled with '0', 'Chinstrap' observation is labeled with '1' 
# and 'Gentoo' observation is labeled with '2'

# Seperating X (features) and Y (target)
x = df.drop('species',axis=1)
y = df['species']

# Now , that we have preprocessed the dataset according to the task at hand we'll now 
# move forward to Building the random forest Classifier Model

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier() 
clf.fit(x,y)

# Saving the Model
'''In Python data science, a pickle file is a serialized file format used for storing 
Python objects in a binary format. It is a way of converting a Python object hierarchy 
into a byte stream that can be stored on disk or transmitted over a network.
The pickle module in Python provides a way to serialize and deserialize Python objects. 
When an object is pickled, it is converted into a binary format that can be stored on 
disk or transmitted over a network. The pickle file extension is typically .pkl or 
.pickle
Pickle files are commonly used in Python data science for caching and persisting machine 
learning models, as well as for storing intermediate results from long-running
computations. By storing these objects in a serialized format, it can help save time by 
avoiding the need to recompute these objects every time they are needed.'''
import pickle
pickle.dump(clf, open('penguins_classification.pkl', 'wb')) # wb -> write binary 