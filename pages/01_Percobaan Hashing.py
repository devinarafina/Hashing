<<<<<<< HEAD
# Imoprt library
=======
>>>>>>> 4aeb01f8942e64b4526cdb4d2bcecea14df9c693
import streamlit as st
import hashlib  # import hashlib module

st.title("Lets Try Hashing!")
text = st.text_input("Input Your Text")

<<<<<<< HEAD
st.title("Let's Try Hashing!")
st.header("Percobaan Hashing")
text = st.text_input("Masukkan data: ")
=======
st.write('Text yang di Input adalah: ',text)
>>>>>>> 4aeb01f8942e64b4526cdb4d2bcecea14df9c693

st.write('Text yang di Input adalah: ',text)
# initialize using sha256
st.header('\nSHA256')
# use the whole string at once
x = hashlib.sha256(text.encode('utf8'))
st.write(x.digest())

# initialize using md5
<<<<<<< HEAD
st.subheader('md5')
=======
st.header('\nmd5')
m = hashlib.md5()

>>>>>>> 4aeb01f8942e64b4526cdb4d2bcecea14df9c693
# use the whole string at once
x = hashlib.md5(text.encode('utf8'))
st.write(x.digest())
