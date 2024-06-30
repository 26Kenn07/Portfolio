import streamlit as st
import time

def show_skills():
    st.header("🎯 Skills")

    # Define the skills and their badge URLs
    skills = [
        {"name": "Python", "badge": "https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"},
        {"name": "Tensorflow", "badge": "https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"},
        {"name": "Pytorch", "badge": "https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"},
        {"name": "Machine Learning", "badge": "https://img.shields.io/badge/machine%20learning-6DA14E?style=for-the-badge"},
        {"name": "Deep Learning", "badge": "https://img.shields.io/badge/deep%20learning-4B8BF5?style=for-the-badge"},
        {"name": "Artificial Intelligence", "badge": "https://img.shields.io/badge/artificial%20intelligence-FF5733?style=for-the-badge"},
        {"name": "FastAPI", "badge": "https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white"},
        {"name": "Flask", "badge": "https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"},
    ]

    # Render a styled box with badges for each skill
    st.markdown(
        """
            <div style="width: 100%; height: 50px; overflow: hidden; white-space: nowrap;">
                <marquee behavior="scroll" direction="left" scrollamount="3">
                """ +
                "".join(f'<a href="{skill["badge"]}"><img src="{skill["badge"]}" alt="{skill["name"]}" height="30"></a>&nbsp;&nbsp;' for skill in skills) +
                """
                </marquee>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="width: 100%; height: 50px; overflow: hidden; white-space: nowrap;">
        <marquee behavior="scroll" direction="right" scrollamount="3">
        """ +
        " ".join(f'<a href="{skill["badge"]}"><img src="{skill["badge"]}" alt="{skill["name"]}" height="30"></a>&nbsp;&nbsp;' for skill in skills) +
        """
        </marquee>
        </div>
        """,
        unsafe_allow_html=True
    )
