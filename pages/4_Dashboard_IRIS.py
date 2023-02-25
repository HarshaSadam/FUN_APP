import streamlit as st
import pandas as pd
from matplotlib import image
import os
import plotly.express as px

st.title("Dashboard - IRIS :hibiscus:")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "iris.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")

img = image.imread(IMAGE_PATH)

st.image(img)

df = pd.read_csv(DATA_PATH)

species = st.selectbox("Select the Iris Species : ",df['Species'].unique())

col1,col2 = st.columns(2)

fig1 = px.histogram(df[df['Species']==species],x ="SepalLengthCm")

fig2 = px.box(df[df['Species']==species],y="SepalLengthCm")

col1.plotly_chart(fig1,use_container_width=True)

col2.plotly_chart(fig2,use_container_width=True)
