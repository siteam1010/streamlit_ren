import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time





st.write('Display Image')
img1 = Image.open('./img/img1.png')
st.image(img1, caption = '写真')

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入






"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
```
"""

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入






if st.checkbox('show Image'):
    img2 = Image.open('./img/img1.png')
    st.image(img2, caption = '押し釦写真')

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入