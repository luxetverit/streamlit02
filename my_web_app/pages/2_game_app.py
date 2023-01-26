import streamlit as st
from PIL import Image 
import os

folder = '../data/'

game_select = ["파이널 판타지 시리즈", "바이오쇼크 인피니트", "바이오하자드 시리즈"]

game_select_option = st.sidebar.selectbox(
    "좋아하는 게임 선택하세요",
    ["파이널 판타지 시리즈", "바이오쇼크 인피니트", "바이오하자드 시리즈"], index=2
)

game_image_files = ['ff7.jpg', 'bioshock.jpg', 'village.jpg']

html = """
<style>
h2 {
    color: skyblue;
    font-style: italic;
}
</style>
"""

st.markdown(html, unsafe_allow_html=True)
st.header(game_select_option)

game_select_index = game_select.index(game_select_option)
st.image(folder + game_image_files[game_select_index])