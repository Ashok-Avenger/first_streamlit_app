import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled free range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# readfile from S3 bucket
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

# setting index from the list file
my_fruit_list = my_fruit_list.set_index('Fruit')

# Allowing user to make a selection from the picklist, giving pre-defined selection
fruits_selected = streamlit.multiselect("Pick some fruits from the picklist below:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the data in streamlist
streamlit.dataframe(fruits_to_show)
