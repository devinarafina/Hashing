import streamlit as st
import hashlib  # import hashlib module

st.title("Lets Try Hashing!")
text = st.text_input("Input Your Text")

st.write('Text yang di Input adalah: ',text)

# initialize using sha256
st.header('\nSHA256')
# use the whole string at once
x = hashlib.sha256(text.encode('utf8'))
st.write(x.digest())

# initialize using md5
st.header('\nmd5')
m = hashlib.md5()

# use the whole string at once
x = hashlib.md5(text.encode('utf8'))
st.write(x.digest())
