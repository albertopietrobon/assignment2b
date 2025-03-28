import streamlit as st

st.title(":green[Give us your feedback] :pencil:")
st.write("> Please fill the form below. **Your feedback is really important for us**.")
form = st.button("Click here for the form")

if form:
    st.switch_page("pages/form.py")

