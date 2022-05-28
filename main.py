from colorama import Style
import streamlit as st
from PIL import Image
import os
import sys
import style 
import pandas as pd
from io import BytesIO, StringIO
st.title("PyTorch Style-Transfer")

style_name = st.sidebar.selectbox(
    'Wähle einen Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img
image_file = st.file_uploader("Upload Image", type=["png", "jpg"])
if image_file is not None:
    file_details = {"filename" :image_file.name,
    "filetype":image_file.type, "filesize":image_file.size}
    with open(image_file.name, "wb") as f:
        f.write(image_file.getbuffer())
    st.image(load_image(image_file))
    input_image = image_file.name
    output_image = "images/output-images/" + style_name + "-" + image_file.name

model = "saved_models/" + style_name + ".pth"





clicked = st.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image:")
    image = Image.open(output_image)
    st.image(image, width=400)

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

