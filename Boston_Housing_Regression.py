import streamlit as st 
import pandas as pd
import shap
# '''SHAP (SHapley Additive exPlanations) is a Python library for interpreting
# the predictions of machine learning models. It provides a unified 
# framework for explaining the output of any model that can be used for
# both classification and regression tasks.
# The library computes Shapley values, which are a way of assigning credit
# to each feature in a prediction.
# Shapley values measure the contribution of each feature value to the
# prediction by estimating the average change in the model's output when a
# feature value is included in a subset of features, compared to the 
# output when the feature value is not included.
# SHAP can be used with a variety of machine learning models, including 
# tree-based models, linear models, and deep neural networks. It is 
# especially useful for models that are difficult to interpret, such as 
# black box models, because it can provide insight into which features are
# most important for making predictions.
# Overall, the SHAP library is a powerful tool for understanding how
# machine learning models make predictions and can be used to improve
# model performance, debug models, and build trust with stakeholders.'''
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.write('''
# Boston House Price Prediction App

This app predicts the ***Boston House Price*
''')
st.write('---')

# Loading the Boston Hous Price data 
boston = pd.read_csv('Boston_Housing.csv',index_col=0)
x = pd.DataFrame(boston.drop(['medv'],axis=1))
y = pd.DataFrame(boston['medv'])
# st.write(x.columns)
# st.write(y.columns)
# st.write(x)
# st.write(y)
# sidebar
# Header to specify the Input Parameters
st.sidebar.header("Specify Input Parameters")

def user_input_features():
    crim = st.sidebar.slider('crim',float(x.crim.min()),float(x.crim.max()),float(x.crim.mean()))
    zn = st.sidebar.slider('zn',float(x.zn.min()),float(x.zn.max()),float(x.zn.mean()))
    indus = st.sidebar.slider('indus',float(x.indus.min()),float(x.indus.max()),float(x.indus.mean()))
    chas = st.sidebar.slider('chas',float(x.chas.min()),float(x.chas.max()),float(x.chas.mean()))
    nox = st.sidebar.slider('nox',float(x.nox.min()),float(x.nox.max()),float(x.nox.mean()))
    rm = st.sidebar.slider('rm',float(x.rm.min()),float(x.rm.max()),float(x.rm.mean()))
    age = st.sidebar.slider('age',float(x.age.min()),float(x.age.max()),float(x.age.mean()))
    dis = st.sidebar.slider('dis',float(x.dis.min()),float(x.dis.max()),float(x.dis.mean()))
    rad = st.sidebar.slider('rad',float(x.rad.min()),float(x.rad.max()),float(x.rad.mean()))
    tax = st.sidebar.slider('tax',float(x.tax.min()),float(x.tax.max()),float(x.tax.mean()))
    ptratio = st.sidebar.slider('ptratio',float(x.ptratio.min()),float(x.ptratio.max()),float(x.ptratio.mean()))
    black = st.sidebar.slider('black',float(x.black.min()),float(x.black.max()),float(x.black.mean()))
    lstat = st.sidebar.slider('lstat',float(x.lstat.min()),float(x.lstat.max()),float(x.lstat.mean()))
    data = {'crim' : crim,
            'zn' : zn,
            'indus' : indus,
            'chas' : chas,
            'nox' : nox,
            'rm' : rm,
            'age' : age,
            'dis' : dis,
            'rad' : rad,
            'tax' : tax,
            'ptratio' : ptratio,
            'black' : black,
            'lstat' : lstat}
    features = pd.DataFrame(data,index=[0]) # index = [0] specifies this is first row 
    return features

df = user_input_features()

# Main Page
# Print the specified Parameters into a DataFrame

st.write('Specified Input Parameters')
st.write(df)
st.write('---')


# Building the Regression Model
model = RandomForestRegressor()
model.fit(x,y)

# Applying the model on the data to make predictions
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# Explaining the model's predictions using the SHAP Values using the 'shap' values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(x)

st.header('Feature Importance')
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, x)
st.pyplot(bbox_inches='tight')
st.write('---')

plt.title('Feature importance based on SHAP values (Bar Plot)')
shap.summary_plot(shap_values, x, plot_type="bar")
st.pyplot(bbox_inches='tight')

# # visualize the first prediction's explanation
# shap.plots.waterfall(shap_values[0])