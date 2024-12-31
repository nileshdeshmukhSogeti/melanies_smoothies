import streamlit as st

# Display the smoothie logo at the top
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Smoothie_logo.svg/1200px-Smoothie_logo.svg.png"  # Replace with your logo URL or local file path
st.image(logo_url, width=200)  # Adjust the width as per your logo size

# Title of the app
st.title("Smoothie Selector")

# Create a dropdown (selectbox) for the user to choose a smoothie type
smoothie_choice = st.selectbox("Select a smoothie to view:", ["Mango Smoothie", "Berry Blast Smoothie", "Green Smoothie", "Tropical Smoothie"])
