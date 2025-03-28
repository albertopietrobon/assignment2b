import streamlit as st

st.title(":green[Give us your feedback] :pencil:")
st.write("> Please fill the form below. **Your feedback is really important for us**.")

with st.form("**USER EXPERIENCE FORM**"):

    name = st.text_input("Full name:", placeholder="Enter you name...")
    rate = st.slider("Rate your satisfaction:",1,5,3)
    comment = st.text_area("Additional comments:", placeholder="Write your comments...")
    
    submitted = st.form_submit_button("Submit")

if submitted:

    if name:
       if comment:
           st.write(f"**:green[Form summary:]**\n\n>*User:* {name}\n\n>*Satisfaction:* {rate}\n\n>*Comment:* {comment}")
           if rate<=2:
               st.warning("We are really sorry you didn't like the experience :cry:")
           if rate>=4:
               st.success("We appreciated a lot your feedback! :smile:")

       else:
           st.write(f"**:green[Form summary:]**\n\n>*User:* {name}\n\n>*Satisfaction:* {rate}\n\n>*Comment:* No further comment")
           if rate<=2:
               st.warning("We are really sorry you didn't like the experience :cry:")
           if rate>=4:
               st.success("We appreciated a lot your feedback! :smile:")
    else:
        st.warning("Missing name! :warning:")




