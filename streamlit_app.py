import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('bog.png'))

st.header('Keeeeeyoti, Ph.D.')

st.info('professional coin flipper')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@keeeeeyoti', 'Keyoti YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/TYKKYTYTK', 'Follow me on Twitter', icon_size)
st_button(' ', 'https://soundcloud.com/keyoti', 'Follow me on Soundcloud', icon_size)
