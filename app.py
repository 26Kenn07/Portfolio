import streamlit as st

from Utils.navigation import navigation_bar
from Utils.typewriter import type_writer
from Utils.show_resume import show_resume
from Utils.inquiries import inquiry
from Utils.contact_info import contact_info
from Utils.achievements import show_achievements
from Utils.custom_css import custom_css_app
from Utils.projects import show_projects
from Utils.skills import show_skills
from Utils.chat import Jarvis

custom_css_app()

# Adding the navigation bar
navigation_bar()

# Adding the main content of the webpage
type_writer()

# Enhanced About Me Section
st.title("🧐 About Me")
st.write("""
As an AI Engineer Intern at Atliq Technologies with a strong foundation in Computer Engineering from Charotar University of Science and Technology. I have expertise in Python, Dart, Machine Learning algorithms and Deep Learning frameworks like PyTorch and TensorFlow. I've excelled in hackathons and recognized as a Kaggle Notebook Expert, demonstrating proficiency in data analysis and machine learning. My skills include data preprocessing, model training, and real-time system implementation.
""")

# Creating columns for layout
col1, col2 = st.columns(2)

with col1:
    # Displaying the resume section
    show_resume()
    

with col2:
    show_skills()
    
# Displaying the project section on the right-hand side of the resume section
show_projects()

# Displaying the achievements section
show_achievements()

Jarvis()

# Displaying the inquiries form
inquiry()

# Displaying the contact information
contact_info()
