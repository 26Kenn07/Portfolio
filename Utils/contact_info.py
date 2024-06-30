import streamlit as st

# Function to display the contact information
def contact_info():
    # Adding contact information to the footer
    st.markdown("""
    <footer>
        <div style="background-color: #333;  margin-top: 50px; padding: 10px;">
            <p style="color: white; text-align: center;">
                Contact: kirtanmatalia@gmail.com | Phone: +91 9898591091
            </p>
        </div>
    </footer>
    """, unsafe_allow_html=True)