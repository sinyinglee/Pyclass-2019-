import streamlit as st
import pandas as pd 
import 

st.title("我的網站")

df = pd.DataFrame({
    "A":[55,12,45],
    "B":[94,87,12]
})

st.write(df)

