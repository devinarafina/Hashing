# Imoprt library
import streamlit as st
import hashlib  # import hashlib module

st.set_page_config(
    page_title="Percobaan Hashing",
    page_icon= "🔏",
)

st.title("Let's Try Hashing!")
st.header("Percobaan Hashing")
text = st.text_input("Masukkan data: ")

st.write('Text yang di Input adalah: ',text)
# initialize using sha256
st.subheader('SHA256')
# use the whole string at once
x = hashlib.sha256(text.encode())
st.write(x.hexdigest())

# initialize using md5
st.subheader('md5')
# use the whole string at once
x = hashlib.md5(text.encode())
st.write(x.hexdigest())