import streamlit as st

# Display the smoothie logo at the top
logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Smoothie_logo.svg/1200px-Smoothie_logo.svg.png"  # Replace with your logo URL or local file path
st.image(logo_url, width=200)  # Adjust the width as per your logo size

# Title of the app
st.title("Smoothie Selector")

# Create a dropdown (selectbox) for the user to choose a smoothie type
smoothie_choice = st.selectbox("Select a smoothie to view:", ["Mango Smoothie", "Berry Blast Smoothie", "Green Smoothie", "Tropical Smoothie"])

import os
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Snowflake connection details from environment variables
user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")
account = os.getenv("SNOWFLAKE_ACCOUNT")
warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
database = os.getenv("SNOWFLAKE_DATABASE")
schema = os.getenv("SNOWFLAKE_SCHEMA")

# Establish Snowflake connection
def create_connection():
    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        return None