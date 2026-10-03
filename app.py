import streamlit as st
import pandas as pd
import time

st.title("Startup Dashboard")
st.header("I am Learning Streamlit")
st.subheader("And I am loving it")
st.write("This is a normal text")
st.markdown("""
### My favourite movies
- Race 3
- Humshakal
- Housefull
""")

st.code("""
def foo(input):
    return input**2

x=foo(2)    
""")

st.latex("x^2+y^2=c^2")

df=pd.DataFrame({
    "name":["Pranav","Rupak raj","Abdul Qadir"],
    "marks":[50,60,70],
    "package":[10,20,30]
})

st.dataframe(df)

st.metric("Revenue","Rs 3","-3%")
st.json({
    "name":["Pranav","Rupak raj","Abdul Qadir"],
    "marks":[50,60,70],
    "package":[10,20,30]
})



st.write("Song Bata ab jaaaye kahan")
st.audio("/home/codex/Desktop/Python/image/audio/Deewana Kar Raha Hai- slowed and reverb - axonnaru.mp3")
st.sidebar.title("Side Bar")
col1,col2=st.columns(2)
with col1:
    st.image("/home/codex/Desktop/Python/image/Screenshot from 2026-09-04 01-04-45.png")

with col2:
    st.video("/home/codex/Desktop/Python/image/video/संघर्ष चुनो! __ आचार्य प्रशांत.mp4")

st.error("Login Failed")
st.success("Login Successful")
bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email=st.text_input("Enter Email") 
number=st.number_input("Enter the image")
date=st.date_input("Enter the date")
   