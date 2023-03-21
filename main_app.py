import streamlit as st
from PIL import Image

# タイトル
st.title('ネコぱふぇアプリ')
st.caption('これはネコぱふぇのテストアプリです')

# 画像
image = Image.open('./data/nekopafe1.png')
st.image(image, width=200)

