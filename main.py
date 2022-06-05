import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('DataFrame')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


'Done!!'


#
#left_column, right_column = st.columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('右カラム')
#
#expander = st.expander('問い合わせ')
#expander.write('問い合わせ内容1')
#expander.write('問い合わせ内容2')
#expander.write('問い合わせ内容3')

#condition = st.slider('あなたの今の調子は？',0,100,50)
#'コンディション：',condition
#
#option1 = st.text_input(
#    'あなたの趣味をおしえてください'
#)
#'あなたの趣味は', option1 ,'です'


#option = st.selectbox(
#    'あなたが好きな好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたの好きな数字は、' , option, 'です'

#if st.checkbox('show image'):
#    img = Image.open('F2A52038-B6E8-41CE-BFFF-42B41CC1B36Cのコピー.jpeg')
#    st.image(img, caption='reo yamagishi', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns=['lat','lon']
#)

#st.dataframe(df, width = 300, height = 100)

#st.dataframe(df.style.highlight_max(axis = 0))

#st.map(df)
