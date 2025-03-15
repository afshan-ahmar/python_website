import streamlit as st
import openai 

import pandas as pd
import plotly.express as px

# Set Streamlit Page Configurations
st.set_page_config(page_title="My Awesome App", page_icon="🚀", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {background-color: #B59BBF;}
    .stSidebar {background-color: #586e75 !important;}
    .stButton>button {background-color: #DCABEF; color: white;}
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🌟 Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Data Visualization", "Chatbot", "Contact Us"])

if menu == "Home":
    st.title("🚀 Welcome to My Streamlit App!")
    st.write("This is a beautiful and feature-rich Streamlit app with an interactive UI.")
    st.image("image.png", use_container_width=True)

elif menu == "Data Visualization":
    st.title("📊 Data Visualization")
    st.write("Upload a CSV file to visualize data.")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Preview Data")
        st.dataframe(df.head())
        column = st.selectbox("Select Column for Visualization", df.columns)
        fig = px.histogram(df, x=column)
        st.plotly_chart(fig)

elif menu == "Chatbot":
    st.title("💬 AI Chatbot")
    openai.api_key = "kv3uan5t"  # Replace with OpenAI API key
    user_input = st.text_input("Ask me anything:")
    if st.button("Send"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("🤖 Bot:", response['choices'][0]['message']['content'])

elif menu == "Contact Us":
    st.title("📧 Contact Us")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Submit"):
        st.success("Thank you for reaching out! We will get back to you soon.")
