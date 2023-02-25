from numpy import histogram
import streamlit as st
import pandas as pd
from matplotlib import image
import os
import plotly.express as px

st.title("Dashboard - TITANIC :ship:")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)

st.image(img)

df  = pd.read_csv(DATA_PATH)

sex = st.selectbox("Select the gender",df['sex'].unique())

col1,col2 = st.columns(2)

fig1 = px.histogram(df[df['sex']==sex], x='class')
fig2 = px.box(df[df['sex']==sex], y='age')

col1.plotly_chart(fig1,use_container_width=True)
col2.plotly_chart(fig2,use_container_width=True)

survied = st.selectbox("Choose for Survival : ",["Survived","Not Survived"])
s=True
if(survied=="Not Survived"):
    s=False

col3,col4 = st.columns(2)

fig3 = px.histogram(df[df['survived']==s], x='age')
fig4 = px.box(df[df['survived']==s], y='age')

col3.plotly_chart(fig3,use_container_width=True)
col4.plotly_chart(fig4,use_container_width=True)

