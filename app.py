import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQnxMS3my42BtJpFyxl1A0y9fYN7HiBB7tnjEOzPQ528okNH88F_Ad6KHXPdPbboV613m1A-z7DbpbO/pub?output=csv"
df = load_data(data_url)

# Display each column with an appropriate visualization
for column in df.columns:
    st.write(f"## {column}")  # Display the column name as a header

    # Check the data type and contents of the column to decide on visualization
    if df[column].dtype == 'object':  # Categorical data
        # Check if the column contains free text responses or multiple choice
        if df[column].nunique() < 10:  # Assuming multiple choice for simplicity
            count_series = df[column].value_counts()
            fig = px.bar(count_series, title=f"{column} Distribution", labels={'value':'Count', 'index':column})
            st.plotly_chart(fig)
        else:
            st.write("Text responses summary:")
            st.write(df[column].value_counts().head(10))  # Show top 10 responses for brevity
    else:  # Numeric data
        fig = px.histogram(df, x=column, title=f"{column} Distribution")
        st.plotly_chart(fig)

    st.write("---")  # Add a separator line