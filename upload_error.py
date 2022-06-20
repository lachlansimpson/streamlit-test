import streamlit as st
import os

def save_uploadedfile(uploadedfile):
     with open(os.path.join("/tmp/streamlit/",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

bytes_data=0

st.config.set_option("server.maxUploadSize", 5000)

uploaded_file = st.file_uploader('Upload Large File')

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.success('Uploaded Successfully')
    save_uploadedfile(uploaded_file)
