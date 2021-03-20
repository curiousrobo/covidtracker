import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings(action='ignore')


class rawData:
    @st.cache(allow_output_mutation=True)
    def get_data(self):
        url = 'https://api.covid19india.org/csv/latest/state_wise.csv'
        return pd.read_csv(url)