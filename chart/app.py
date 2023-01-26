import streamlit as st
from PIL import Image 
import os

st.title("멀티 페이지 웹 앱")

st.subheader("사이드바에서 페이지를 선택하세요.")
st.subheader("- chart1")
st.subheader("- chart2")
st.subheader("- chart3")
st.markdown(
    """
    <style>
    [data-testid="stSidebar][aria-expanded="true"] > div:first-child{width:250px;}</style>
    """, unsafe_allow_html=True
)

