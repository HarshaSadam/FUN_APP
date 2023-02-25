from pyparsing import col
from pytz import country_names
import streamlit as st
import pandas as pd
from matplotlib import image
import os
import plotly.express as px

st.title("Dashboard - TIPS :necktie:")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "tips.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

img = image.imread(IMAGE_PATH)

st.image(img,use_column_width=True)

df = pd.read_csv(DATA_PATH)

time  = st.selectbox("Select the Time of Food : ",df['time'].unique())
fig_1 = px.histogram(df[df['time']==time], x="total_bill")
fig_2 = px.box(df[df['time']==time], y="total_bill")

col1,col2 = st.columns(2)

col1.plotly_chart(fig_1, use_container_width=True)
col2.plotly_chart(fig_2, use_container_width=True)
