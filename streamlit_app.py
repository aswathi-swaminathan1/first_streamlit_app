import streamlit

streamlit.title("My Mom's New Healthy Dinner")
streamlit.title("Breakfast Favourites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 kale, Spinach & rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-Range Egg")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.title("🍌🥭 Build Your Own Fruit Smoothie 🥝 🍇")
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

