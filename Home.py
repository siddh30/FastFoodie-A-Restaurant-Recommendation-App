import streamlit as st
import streamlit as st
from PIL import Image

st.set_page_config(layout='centered', initial_sidebar_state='expanded')

st. sidebar.image('Data/App_icon.png')

image = Image.open('Data/Food.png')
st.image(image, use_column_width=True)
st.warning("The app to get you to the closest and most highly rated places to eat!")
st.markdown("Based on data from TripAdvisor, the app covers restaurants form 20 cities across New York, New Jersey, California, Texas and Washington to recommend the 10 most similar restaurants to the one you like. ")
st.markdown("This app uses Natural Language Processing and Content Based Recommender Systems with focusing on user comments as the main feature.")
st.success("Because hunger is also an emergency!! :ambulance:" ":100:")
