import streamlit as st

def inquiry():
    
    st.title("✉️ Contact Me")

    # Custom CSS for the inquiry form
    st.markdown("""
    <style>
        /* Form Styling */
        form {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: black;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add box shadow */
        }
        
        /* Styling for form inputs and textarea */
        form input, form textarea, form button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            color: black;
            font-size: 1em;
        }
        
        /* Set background color for inputs and textarea */
        form input, form textarea {
            background-color: #f0f0f0;  /* Light gray background */
        }

        /* Focus effect for inputs and textarea */
        form input:focus, form textarea:focus {
            border-color: #007BFF;
            outline: none;
            box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
        }
        
        /* Styling for the submit button */
        form button {
            background-color: #FF0000;
            color: black;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        /* Hover effect for the submit button */
        form button:hover {
            background-color: green;
        }
    </style>
    """, unsafe_allow_html=True)

    contact_form = """
    <form action="https://formsubmit.co/kirtanmatalia@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)