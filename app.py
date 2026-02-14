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
        color: #d63384 !important; /* Forced Pink */
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }
    .love-text {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4a4a4a !important; /* Forced Dark Gray/Black */
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
    }
    /* This forces all regular Streamlit text to stay dark */
    .stMarkdown, p, div, label {
        color: #31333F !important; 
    }
    /* Style for the subheaders */
    h3, h2, h1 {
        color: #d63384 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5) # Add a timeout
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Use a confirmed working Lottie URL (Heart animation)
lottie_url = "https://lottie.host/855905d5-8675-4009-8f0a-115f0133c94f/v7C0pI3C8O.json"
lottie_heart = load_lottieurl(lottie_url)

# --- HEADER ---
if lottie_heart:
    st_lottie(lottie_heart, height=200, key="coding")
else:
    st.write("💖") # Fallback to an emoji if the animation fails to load

st.markdown("<h1 class='main-title'>Happy Valentine's Day, Komal!</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='love-text'>From your favorite Data Scientist, <b>Himanshu</b></p>", unsafe_allow_html=True)

# --- REASONS SECTION ---
st.write("---")
st.subheader("🌸 Why I Love You")
reasons = [
    "✨ You are so sweet, you are awesome.",
    "🏡 You make me feel so comfortable, anywhere feels like home.",
    "🌟 You are the best partner I could have asked for."
]
for reason in reasons:
    st.write(f"❤️ {reason}")

# --- PHOTO GALLERY ---
st.write("---")
st.subheader("📸 Our Best Moments")

# List of your photos and their Hinglish captions
photo_data = [
    {"img": "photo1.jpg", "caption": "Humaari chemistry ka koi competition hi nahi hai! 🔥"},
    {"img": "photo2.jpg", "caption": "Komal + Himanshu = The Perfect Model. 👩‍❤️‍👨"},
    {"img": "photo3.jpg", "caption": "Tumhaari smile hi meri real success metric hai. ✅"}
]

cols = st.columns(3)

for i, col in enumerate(cols):
    with col:
        # Display the image with the Hinglish caption
        st.image(
            photo_data[i]["img"], 
            use_container_width=True, 
            caption=photo_data[i]["caption"]
        )

# --- THE PROPOSAL SECTION ---
st.write("---")
st.markdown("<h3 style='text-align: center;'>Will you be my Valentine? 🌹</h3>", unsafe_allow_html=True)

col_yes, col_no = st.columns(2)

with col_yes:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("Yay! I knew you'd say yes! You're stuck with me forever now. Ab main tumhaara aur humaare nanhe 'Junior' ka khayal rakhne ke liye taiyaar hoon! 🍝🥂")
        st.snow()

with col_no:
    if st.button("No ❌"):
        st.error("Error 404: Choice not found. Sorry, that's not gonna happen! Try again. 😉")
        st.warning("Hint: There is only one right answer here!")