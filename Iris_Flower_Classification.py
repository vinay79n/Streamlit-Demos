import streamlit as st  
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Classification App

this app perdictsthe Iris flower type""")

st.sidebar.header('User Input Options')

def user_input_features():
    sepel_length = st.sidebar.slider('sepel length', 4.3, 7.9, 5.4)
    sepel_width = st.sidebar.slider('sepel width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal length', 1.0,6.9, 1.3)
    petal_width = st.sidebar.slider('petal width', 0.1, 2.5, 0.2)
    data = {'sepel_length': sepel_length,
            'sepel_width': sepel_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data,index=[0]) 
    return features  

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

Iris = datasets.load_iris()
x = Iris.data
y = Iris.target

clf = RandomForestClassifier()
clf.fit(x,y)

predictions = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(Iris.target_names)

st.subheader('Predictions')
st.write(Iris.target_names[predictions])

st.subheader('Prediction Proabability')
st.write(prediction_proba)