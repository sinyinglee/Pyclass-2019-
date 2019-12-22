import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("my plot web")
st.markdown(r"畫一個 ＄\dfrac{\sin(x)}{x}$") #markdown格式有誤
x = np.linspace(-10,10,200)
y = np.sinc(x)
plt.plot(x,y)
st.pyplot()