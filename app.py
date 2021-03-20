import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')
from plots import tablePlot
from data import rawData
from preprocess import rawDataPreprocess


st.markdown("<h1 style='text-align: center; color: #000000'>COVID19 TRACKER</h1>",
                        unsafe_allow_html=True)
st.sidebar.title('Select View')

st.sidebar.selectbox('', ['Overall', 'Spread Trend', 
                          'Statewise Comparison', 'Testing Status', 
                          'Vaccination Status', 'Bed Status'])
rawData = rawData()
df = rawData.get_data()

rawDataPreprocess = rawDataPreprocess()
df_overall = rawDataPreprocess.overall(df)
df_daily = rawDataPreprocess.daily(df)

overall_or_daily = st.selectbox('',['Overall', 'Daily'])

tablePlot = tablePlot()
if overall_or_daily == 'Overall':
    tablePlot.table(df_overall)
else:
    tablePlot.table(df_daily)
