import streamlit as st

# Function to add a navigation bar with icons and links
def navigation_bar():
    st.sidebar.image("/Users/kirtan/Downloads/Portfolio/MyData/Kirtan Matalia.jpg", caption="Kirtan Matalia", use_column_width=True)
    
    # Kaggle icon with link
    st.sidebar.markdown("""
        <a href="https://www.kaggle.com/kirtanmatalia26" target="_blank" class="icon kaggle" style="background-color: #000000;">
            <img src="https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png" height="30" alt="Kaggle">
        </a>
    """, unsafe_allow_html=True)
    
    # Gmail icon with link
    st.sidebar.markdown("""
        <a href="mailto:kirtanmatalia@gmail.com" target="_blank" class="icon gmail" style="background-color: #FFFFFF;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" height="30" alt="Gmail">
        </a>
    """, unsafe_allow_html=True)
    
    # LinkedIn icon with link
    st.sidebar.markdown("""
        <a href="https://www.linkedin.com/in/kirtan-matalia/" target="_blank" class="icon linkedin" style="background-color: #0077B5;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" height="30" alt="LinkedIn">
        </a>
    """, unsafe_allow_html=True)
    
    # GitHub icon with link
    st.sidebar.markdown("""
        <a href="https://github.com/26Kenn07" target="_blank" class="icon github" style="background-color: #FFFFFF;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" height="30" alt="GitHub">
        </a>
    """, unsafe_allow_html=True)
    
     # Medium icon with link
    st.sidebar.markdown("""
        <a href="https://medium.com/@kirtanmatalia" target="_blank" class="icon medium" style="background-color: #000000;">
            <img src="https://miro.medium.com/v2/resize:fit:1000/format:webp/1*Ra88BZ-CSTovFS2ZSURBgg.png" height="30" alt="Medium">
        </a>
    """, unsafe_allow_html=True)
    
    # LeetCode icon with link
    st.sidebar.markdown("""
        <a href="https://leetcode.com/kirtanmatalia/" target="_blank" class="icon leetcode" style="background-color: #FFFFFF;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png" height="30" alt="LeetCode">
        </a>
    """, unsafe_allow_html=True)