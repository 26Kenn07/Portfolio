import streamlit as st

def custom_css_app():
    # Custom CSS for the entire app
    st.markdown("""
    <style>
        /* Remove default padding */
        .reportview-container .main .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        
        /* Set background color for main container */
        .reportview-container {
            background: white;
        }
        
        /* Set background color for sidebar */
        .sidebar .sidebar-content {
            background: #333;
        }
        
        /* Set text color for sidebar buttons */
        .sidebar .sidebar-content button {
            color: white;
        }
        
        /* Set background and text color for header and footer */
        .header, .footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
        
        /* Additional styling for icons */
        .icon {
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-decoration: none;
            margin-bottom: 10px;
            border-radius: 5px;
            padding: 5px;
            transition: filter 0.3s ease;
        }
        
        /* Add margin to icon images */
        .icon img {
            margin-right: 10px;
        }
        
        /* Add hover effect to icons */
        .icon:hover {
            filter: brightness(85%);
            background-color: transparent; /* Resetting background on hover */
        }

        /* CSS for fixed-size boxes */
        .box {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px 0;
            background-color: #f9f9f9;
            height: 300px;  /* Fixed height for the box */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        
        /* Styling for box headers */
        .box h3 {
            margin: 0;
            font-size: 1.2em;
            font-weight: bold;
        }
        
        /* Limit the image size in the box */
        .box img {
            max-width: 100%;
            height: auto;
            max-height: 150px;  /* Fixed height for the image */
            margin-bottom: 10px;
        }
        
        /* Styling for box paragraphs */
        .box p {
            margin: 0;
            font-size: 0.9em;
        }
        
        /* Responsive styling for boxes */
        @media (max-width: 768px) {
            .box {
                height: auto;  /* Adjust height for smaller screens */
                padding: 20px;  /* Increase padding for better spacing */
                margin-bottom: 20px;  /* Add margin bottom for spacing */
            }
            .box img {
                max-width: 100%;
                max-height: 200px;  /* Adjust image size for smaller screens */
            }
        }
        
        
    """, unsafe_allow_html=True)