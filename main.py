import time

import pyautogui
import streamlit as st
import pywhatkit as kit

import pandas as pd


st.title("WhatsApp Automation")

url=st.text_input(label="Enter Your Url Here",value="https://alquran-45.streamlit.app/")

msg=st.text_area(label="Enter Your Url Here",value="Follow Me On This web")

MeriUploadFile=st.file_uploader("Upload a file",type=["xlsx"])


if MeriUploadFile is not None:
    st.write("Contacts Are Uploaded")

    df=pd.read_excel(MeriUploadFile)

    st.dataframe(df)

    if st.button("Send Message"):

        for i , row in df.iterrows():

            phoneNumber=f"+92{row["Phone"]}"
            customMessage=f"{msg}\n{url}"


            kit.sendwhatmsg_instantly(phone_no=phoneNumber,message=customMessage,wait_time=15)

            time.sleep(15)
            pyautogui.press("enter")

            time.sleep(15)
            pyautogui.press("enter")

st.success("copyright alright reserved by M.Mubashir khan")

