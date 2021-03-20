import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings(action='ignore')

class rawDataPreprocess:
    def overall(self, df):
        excluded_rows = ['State Unassigned', 'Total']
        df = df[~df['State'].isin(excluded_rows)]
        df = df[['State', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'Last_Updated_Time']]
        df.rename(columns={'Last_Updated_Time':'Last Updated'}, inplace=True)
        df.sort_values(by=['Active', 'Confirmed', 'Recovered', 'Deaths'], ascending=False, inplace=True)
        return df
    
    def daily(self, df_daily):
        excluded_rows = ['State Unassigned', 'Total']
        df_daily = df_daily[['State', 'Last_Updated_Time', 'Delta_Confirmed', 'Delta_Recovered', 'Delta_Deaths']]
        df_daily = df_daily[~(df_daily['State'].isin(excluded_rows))]
        df_daily.rename(columns={'Delta_Confirmed':'Confirmed',
                                'Delta_Recovered':'Recovered',
                                'Delta_Deaths':'Deaths'}, inplace=True)
        df_daily.sort_values(by=['Confirmed', 'Recovered', 'Deaths'], ascending=False, inplace=True)
        return df_daily
