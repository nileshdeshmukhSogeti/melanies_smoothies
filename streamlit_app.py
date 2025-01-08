# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
#Header 

st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    "Choose the fruits you want in your custom Smoothie!"
)


name_on_order = st.text_input("Name on Smoothie")
st.write("This name will be on Smoothie", name_on_order)



cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))#**To select only specific col data from a table 
st.dataframe(data=my_dataframe, use_container_width=True) #**To draw the table using data from my_dataframe
st.stop()



ingredients_list = st.multiselect (
    'Choose up to 5 ingredients:'
    , my_dataframe
    , max_selections = 5
    )
ingredients_string = '' 
time_to_insert = '' 

if ingredients_list: #Handle indent of visuals if ingredients_list is not null: then do everything below this line that is indented. 
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = '' 
    for fruit_chosen in ingredients_list: 
        ingredients_string += fruit_chosen + ' ' #+= add text to earlier selected text in loop
        st.subheader(fruit_chosen + ' Nutrition Information')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)
        sf_df = st.dataframe(data=smoothiefroot_response.json(),use_container_width= True)
        #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
                values ('""" + ingredients_string + """','""" +name_on_order+"""')"""

    #st.write(my_insert_stmt)
    #st.stop() #This helps for troubleshotting code
    time_to_insert = st.button('Submit Order')
    
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")


