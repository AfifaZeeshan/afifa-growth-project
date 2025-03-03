# streamlit
import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Title and introduction
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌞")

# Quote section
st.header(" 💡 Today's Growth Mindset Quote")
st.write(" ❝Success is not final, failure is fatal: it is the courage that counts.❞ - Winston Churchill")

# Challenge input section
st.header(" 🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Conditions for the challenge section
if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("Reflect Your Learning!")
reflection = st.text_area("Write your reflections here:")

# Conditions for the reflection section
if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience helps you grow! Share your difficulties.")

# Achievement section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

# Conditions for the achievement section
if achievement:
    st.success(f" 🎉 Amazing! You have achieved: {achievement}")
else:
    st.info("Big or Small, every achievement counts! Share one now! 😎")

# Footer section
st.write("- - -")
st.write(" 🚀 Keep believing in yourself. Growth is a journey, not a destination! ☀️")
st.write("** ⛔ Created by Afifa Zeeshan**")
