import streamlit as st
from PIL import Image 
import os

st.title("멀티 페이지 웹 앱")

st.subheader("사이드바에서 페이지를 선택하세요.")
st.subheader("- drama_app: 좋아하는 드라마 목록")
st.subheader("- game_app: 좋아하는 게임 목록")
st.subheader("- picture_app: 사진찍기")
st.markdown(
    """
    <style>
    [data-testid="stSidebar][aria-expanded="true"] > div:first-child{width:250px;}</style>
    """, unsafe_allow_html=True
)

