from rembg import remove
import streamlit as st

images = st.file_uploader("Drag and Drop the image", type = ['png', 'jpg', 'jpeg'], accept_multiple_files=True)
for image in images:
    image = image.read()
    output = remove(image)
    st.image(output, caption='Output', use_column_width=True)
    st.download_button("Download", output, "output.png", "image/png", key="download_button")