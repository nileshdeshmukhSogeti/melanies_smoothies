# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
#Header 

st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    "Choose the fruits you want in your custom Smoothie!"
)


name_on_order = st.text_input("Name on Smoothie")
st.write("This name will be on Smoothie", name_on_order)

