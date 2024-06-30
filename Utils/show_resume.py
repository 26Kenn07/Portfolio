import streamlit as st
import fitz

def show_resume():
    st.header("📄 Resume")
    resume_path = "MyData/Kirtan_Resume.pdf"
    
    if st.button("Preview Resume..."):
        # Open the PDF file
        document = fitz.open(resume_path)
        
        # Loop through pages and display as images
        for page_number in range(len(document)):
            page = document.load_page(page_number)
            
            # Render page as image with higher DPI for clarity
            zoom = 2.0  # Increase zoom factor for higher DPI rendering
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            image_bytes = pix.tobytes()
            st.image(image_bytes, use_column_width=True)
            
    
    # Download button for the resume
    with open(resume_path, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Kirtan_Resume.pdf",
            mime="application/pdf"
        )