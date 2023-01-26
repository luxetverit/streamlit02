import streamlit as st
from PIL import Image 
import os

drama_select = ["언내추럴", "MIU404", "도망치는 건 부끄럽지만 도움이 된다"]

drama_select_option = st.sidebar.selectbox(
    "좋아하는 드라마를 선택하세요",
    ["언내추럴", "MIU404", "도망치는 건 부끄럽지만 도움이 된다"], index=2
)

folder = '../data/'

image_files = ['un.jpg', 'MIU404.jpg', 'nigehaji.png']

html = """
<style>
h2 {
    color: skyblue;
    font-style: italic;
}
</style>
"""

# 사이드바에 있는 다라마 리스트의 0, 1, 2 순서에 맞춰 텍스트 데이터 호출
st.markdown(html, unsafe_allow_html=True)
st.header(drama_select_option)

# 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용
drama_select_index = drama_select.index(drama_select_option)

#st.write(drama_select_index)
st.image(folder + image_files[drama_select_index])