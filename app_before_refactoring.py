import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

drama_select = ["언내추럴", "MIU404", "도망치는 건 부끄럽지만 도움이 된다"]

drama_select_option = st.sidebar.selectbox(
    "좋아하는 드라마를 선택하세요",
    ["언내추럴", "MIU404", "도망치는 건 부끄럽지만 도움이 된다"], index=2
)

folder = './data/'

[col1, col2] = st.columns(2) 

with col1:
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

with col2:
    game_select = ["파이널 판타지 시리즈", "바이오쇼크 인피니트", "바이오하자드 시리즈"]

    game_select_option = st.sidebar.selectbox(
        "좋아하는 게임 선택하세요",
        ["파이널 판타지 시리즈", "바이오쇼크 인피니트", "바이오하자드 시리즈"], index=2
    )

    game_image_files = ['ff7.jpg', 'bioshock.jpg', 'village.jpg']

    st.markdown(html, unsafe_allow_html=True)
    st.header(game_select_option)

    game_select_index = game_select.index(game_select_option)
    st.image(folder + game_image_files[game_select_index])

import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)

# 보통 사이드바 / 메뉴는 주제별로 서비스를 분류할 때 쓰임
# 1) 드라마 좋아하는 목록 
# 2) 게임 좋아하는 목록
# 3) 사진찍기

# 1. 하나의 파일에 3개를 다 집어넣고 클릭할 때마다 해당 div만 보이게 만들기
# 2. 각 기능별로 별도 파일 혹은 폴더로 만든 후, 클릭시 해당 파일에 들어가도록 만들기
# 보통은 2번을 많이 사용 > 1_drama_app.py, 2_game_app.py, 3_picture_app.py 3개로 파일 분리하기
# streamlit run 1_drama_app.py
# streamlit run 2_game_app.py
# streamlit run 3_picture_app.py
