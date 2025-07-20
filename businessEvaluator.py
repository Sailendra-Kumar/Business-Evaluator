import streamlit as st
import google.generativeai as genai
genai.configure(api_key='Your_API_Key')
mymodel=genai.GenerativeModel('gemini-1.5-flash',system_instruction='''i will give a business idea and small description
about my idea, they will be sepaerated by a ;. you have to generate a report with the following
1. Business Overview
 2. Market research
 3. launch and scale
 4. ways to raise capital''')
myChat=mymodel.start_chat()
st.title("Business Evaluator")
title = st.text_input("enter a title")
description=st.text_area("enter description")
question=title+';'+description
if st.button("submit"):
    # myChat = mymodel.start_chat()
    response = myChat.send_message(question)
    st.write(response.text)
