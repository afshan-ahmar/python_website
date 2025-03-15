import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

# Set Page Config
st.set_page_config(page_title="Build a Python Website in 15 Min!", page_icon="🚀", layout="wide")

# Header with Animation
def main():
    st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        color: #FF4B4B;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #4B4BFF;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='main-title'>🚀 Build a Python Website in 15 Min with Streamlit! 🚀</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Quick, Easy & Beautiful Web Apps with Python</p>", unsafe_allow_html=True)
    
    rain(emoji="✨", font_size=20, falling_speed=5, animation_length=2)
    
    # Sidebar for Navigation
    with st.sidebar:
        st.header("📌 Navigation")
        page = st.radio("Go to:", ["Introduction", "Installation", "Building the App", "Deployment"])
    
    if page == "Introduction":
        show_introduction()
    elif page == "Installation":
        show_installation()
    elif page == "Building the App":
        show_building_app()
    elif page == "Deployment":
        show_deployment()

def show_introduction():
    colored_header("💡 Why Streamlit?", color_name="blue-70")
    st.write("Streamlit is the fastest way to create data apps using Python. It’s simple and requires no front-end experience!")
    st.image("https://docs.streamlit.io/en/stable/_static/img/header-logo.svg", width=250)

def show_installation():
    colored_header("🛠 Installation Steps", color_name="red-70")
    st.code("""
    # Install Streamlit
    pip install streamlit
    
    # Run a sample app
    streamlit hello
    """, language="bash")

def show_building_app():
    colored_header("🚧 Let's Build Our App!", color_name="green-70")
    st.write("Below is a simple Streamlit app:")
    st.code("""
    import streamlit as st
    
    st.title("Hello, Streamlit!")
    st.write("This is a simple web app built in Python.")
    
    if st.button("Click Me!"):
        st.success("You clicked the button!")
    """, language="python")

def show_deployment():
    colored_header("🚀 Deploy Your App!", color_name="purple-70")
    st.write("Deploying on Streamlit Cloud is easy:")
    st.code("""
    1. Push your code to GitHub
    2. Go to [Streamlit Cloud](https://share.streamlit.io)
    3. Connect your repository and deploy!
    """)
    st.balloons()
    
if __name__ == "__main__":
    main()
