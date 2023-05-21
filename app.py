import streamlit as st
import pandas as pd

# Set up sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Home", "Model"])

# Set up page title
st.title("Auto-Data")

# Set up page content
if page == "Home":
    st.write("Welcome to Auto-Data!")
    st.write("This is a simple web app that allows you to upload and explore data.")
    st.write("Navigate to the Model page to see how the model works.")
elif page == "Model":
    st.write("Upload your dataset below:")
    uploaded_file = st.file_uploader("Choose a file", type=("csv", "xlsx", "json"))
    if uploaded_file is not None:
        # Read the uploaded file using pandas
        try:
            if uploaded_file.name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            elif uploaded_file.name.endswith('json'):
                df = pd.read_json(uploaded_file)
        except Exception as e:
            st.write('Error:', e)
        else:
            # Display the dataframe
            st.write("Here's your dataframe:")
            st.write(df)