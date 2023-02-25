from pytz import country_names
import streamlit as st
import pandas as pd
from matplotlib import image
import os
import plotly.express as px

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "climate_change.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Temperature_change_Data.csv")

st.title("Dashboard - Climate Change :tornado_cloud:")

img = image.imread(IMAGE_PATH)

st.image(img,use_column_width=True)

df = pd.read_csv(DATA_PATH)

country_names = st.selectbox("Select the Country:", df['Country Name'].unique())


fig_1 = px.histogram(df[df['Country Name']==country_names], x="tem_change")


st.plotly_chart(fig_1, use_container_width=True)
