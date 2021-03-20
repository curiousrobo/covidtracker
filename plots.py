import pandas as pd
import numpy as np
import streamlit as st
import warnings
import plotly.graph_objects as go
warnings.filterwarnings(action='ignore')

class tablePlot:
    def table(self, df):
        cols=list(df.columns)
        fig = go.Figure(data=[go.Table(
            header=dict(values=cols,
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df[col_nm] for col_nm in cols],
                    fill_color='lavender',
                    align='left'))
        ])
        fig.update_layout(width=800, height=1000,
                        margin=dict(l=0, r=70, b=40, t=40))
        st.plotly_chart(fig)