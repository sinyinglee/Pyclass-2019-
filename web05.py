import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

city = st.selectbox("居住地",["台北市",
                           "台中市",
                           "高雄市",
                           "台南市"])

st.write(f"你選擇了{city}!")
