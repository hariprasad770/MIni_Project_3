import pandas as pd
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
 
data = pd.read_csv('C:/Users/DEEPADHARSHINI/OneDrive/Desktop/Cleaned_Crop_data.csv')


st.title("Crop Production Prediction App")
st.write("### Dataset Preview")
st.dataframe(data.head())
