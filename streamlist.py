import streamlit as st 
# Set the app title 
st.title('My First Streamlit App') 
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 
# Create a text input 
user_input = st.text_input('Enter a custom message:') 
# Display the customized message 
st.write('Customized Message:', user_input)

import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

# Add a slider
slider_val = st.slider('Select a range', 0, 10)

# Filter the dataframe
filtered_df = df[df['A'] > slider_val]

# Display the dataframe
st.write(filtered_df)
st.line_chart(df)

file = st.file_uploader("Pick a file")