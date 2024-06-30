import streamlit as st
from PIL import Image  

# Function to display achievements section in two columns with fixed size boxes
def show_achievements():
    st.title("🏆 Achievements")
    
    # List of achievements
    achievements = [
        ("MyData/MGIT.jpeg", "1st position at MGIT, Hyderabad."),
        ("MyData/PUH.jpeg", "Consolation prize at Parul, Vadodara."),
        ("MyData/CVMU.jpeg", "1st prize at CVMU, Anand."),
        ("MyData/MAKERFEST.jpeg", "Silver Award at Makers Fest Vadodara."),
        ("MyData/Gateway1.jpeg", "Exceptional Performer at Gateway, Ahmedabad."),
        ("MyData/TOI-News.jpg","News in Times Of India"),
    ]
    
    col1, col2 = st.columns(2)  # Divide into two columns
    
    for i, (image_path, caption) in enumerate(achievements):
        col = col1 if i % 2 == 0 else col2
        
        with col:
            # Load image
            image = Image.open(image_path)
            image = image.resize((2500, 2000))  
            st.image(image, caption=caption, use_column_width=True)
            st.write('\n')
            st.write('\n')
            st.write('\n')