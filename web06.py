import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

coffee = st.slider("咖啡粉量",
                   10.0, #最小值
                   45.0, #最大值
                   20.0, #default數值
                   0.5) #每次跳的格數
water = 15*coffee
st.write(f"咖啡粉{coffee}克, 請使用{water}g的水")
