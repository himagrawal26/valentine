import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

# Page Config
st.set_page_config(page_title="For My Komal", page_icon="💖", layout="centered")

# --- CUSTOM CSS FOR AESTHETICS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    .main-title {
        font-family: 'Great Vibes', cursive;
        color: #d63384;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0;
    }
    .love-text {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4a4a4a;
        text-align: center;
        font-size: 1.2rem;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 20px;
        border: 2px solid #ff4b4b;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_02p796w4.json")

# --- HEADER ---
st_lottie(lottie_heart, height=200, key="coding")
st.markdown("<h1 class='main-title'>Happy Valentine's Day, Komal!</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='love-text'>From your favorite Data Scientist, <b>Himanshu</b></p>", unsafe_allow_html=True)

# --- REASONS SECTION ---
st.write("---")
st.subheader("🌸 Why I Love You")
reasons = [
    "✨ You are so sweet, you're giving me a sugar rush!",
    "🏡 You make me feel so comfortable, anywhere feels like home.",
    "🌟 You are the best partner I could have asked for."
]
for reason in reasons:
    st.write(f"❤️ {reason}")

# --- PHOTO GALLERY ---
st.write("---")
st.subheader("📸 Our Best Moments")
# Note: Ensure photo1.jpg, photo2.jpg, photo3.jpg are in your GitHub repo
cols = st.columns(3)
photos = ["photo1.jpg", "photo2.jpg", "photo3.jpg"] 

for i, col in enumerate(cols):
    with col:
        # Placeholder logic: change these to your actual file names
        st.image(photos[i], use_container_width=True, caption=f"Memory #{i+1}")

# --- THE PROPOSAL SECTION ---
st.write("---")
st.markdown("<h3 style='text-align: center;'>Will you be my Valentine? 🌹</h3>", unsafe_allow_html=True)

col_yes, col_no = st.columns(2)

with col_yes:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("Yay! I knew you'd say yes! You're stuck with me forever now. I'll start booking the dinner! 🍝🥂")
        st.snow()

with col_no:
    if st.button("No ❌"):
        st.error("Error 404: Choice not found. Sorry, that's not gonna happen! Try again. 😉")
        st.warning("Hint: There is only one right answer here!")