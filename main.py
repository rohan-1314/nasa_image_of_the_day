import streamlit as st
import requests
import api
url = f"https://api.nasa.gov/planetary/apod?api_key={api.api_key}"
request = requests.get(url)
data = request.json()
title = data['title']
content = data['explanation']
url = data['url']
image_req = requests.get(url)
with open('image.png', 'wb') as file:
    file.write(image_req.content)

st.title(title)
st.image('image.png')
st.write(content)
