"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Harvest Quantity Estimation System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Harvest Quantity Estimation system is a user-friendly web application designed for farmers and agricultural enthusiasts to optimize their crop yields by understanding the nutrient requirements of their soil. Our tool allows you to predict harvest production based on essential soil parameters: Nitrogen (N), Phosphorus (P), Potassium (K),mean temperature, rainfall amount and pH value.
        </p>
    """, unsafe_allow_html=True)
