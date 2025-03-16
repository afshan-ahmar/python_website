import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="My Stylish App", layout="wide")

# Custom CSS for attractive UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Load an image for UI enhancement
image = Image.open("image.png")

# Home Page
if page == "Home":
    st.title("Welcome to My Stylish Streamlit App")
    st.image(image, caption="Beautiful UI", use_container_width=True)
    st.write("This is a simple, elegant, and modern web application built with Streamlit.")
    
    # User Input
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to our platform.")
    
    if st.button("Click Me!"):
        st.balloons()

# About Page
elif page == "About":
    st.title("About Us")
    st.write("We aim to build beautiful and user-friendly apps using Python and Streamlit.")
    st.info("Streamlit makes it easy to build and deploy interactive applications!")

# Contact Page
elif page == "Contact":
    st.title("Contact Us")
    st.write("Feel free to reach out!")
    st.text_input("Your Email")
    st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Message Sent Successfully!")
