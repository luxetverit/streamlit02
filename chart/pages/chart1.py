import streamlit as st
import pandas as pd

# chart 1
data1 = [ -2,   5,  -3,  -3,   9,  -4,  -7,  -9,   2,   3]
data2 = [  3,   4,  -4,  -2,  -3,  -2,   0,   7,  -6,   6]
data3 = [-10,   2,   8,   6,  -7,  -1,  -4,  -1,   4,   5]
dict_data = {"data1":data1, "data2":data2, "data3":data3} 

# 데이터프레임으로 만들고 화면에 출력해 보세요 
df = pd.DataFrame(dict_data)

import streamlit as st
import pandas as pd
import numpy as np

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

st.write(df)

import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
