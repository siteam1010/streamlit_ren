import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
##git_test


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





option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入





st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text, ' です。'

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入




st.sidebar.write('Interactive Widgets')
text = st.sidebar.text_input('あなたの年齢を教えてください。')
'あなたの年齢：', text, ' です。'

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入




left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入




expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２回答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３回答')

st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入
st.markdown("<br>", unsafe_allow_html=True)  # 空行を挿入





st.write('プログレスバーの表示')
'Start!!'
latest_interation = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!!!!'





