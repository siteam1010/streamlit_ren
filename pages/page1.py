import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit 入門')

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入





st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3],
    '2列目': [10, 20, 30]
})
st.table(df.style.highlight_max(axis=0))

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
