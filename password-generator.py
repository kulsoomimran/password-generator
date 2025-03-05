import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=25, value=12)

use_digits = st.checkbox("Use Digits")

use_special_chars = st.checkbox("Use Special Characters")

if st.button("Generate Password"):

    password = generate_password(length, use_digits, use_special_chars)
    
    st.success(f"Generated Password: {password}")

st.write('------------------------')

st.write("Made with ❤️ by [Kulsoom Imran](https://github.com/kulsoomimran)")