import streamlit as st

def show_projects():
    st.header("🛠️ Projects")
    
    projects = [
        {
            "title": "👁️ ExamEye",
            "description": "ExamEye is an AI guardian for secure online exams, offering real-time vigilance, smart anti-cheating measures, and robust features like eye gaze tracking, multi-platform compatibility, browser lockdown, real-time alerts, and live chat support which makes it much more worthy to use in various online assessments.",
            "link": "https://drive.google.com/file/d/1kPd9Cv4LrqeUHABiJcU-8ZcBEC5tH20S/view"
        },
        {
            "title": "🏏 Sports Action Detection",
            "description": "Created and curated diverse datasets with 1000+ images encompassing a range of cricketing shots including ’Drive’, ’Pull’, ’Flick’, ’Lofted-Drive’, and ’Reverse-Sweep’, as well as volleyball actions such as ’Service’, ’Setting’, ’Take’, ’Smash’, and ’Block’ & Developed the custom YOLOv8 models for all with 90%+ accuracy.",
            "link": "https://github.com/26Kenn07/Sports_Action_Detection_Using_YOLO"
        },
        {
            "title": "🤖 Jarvis",
            "description": "Jarvis is an advanced chatbot assistant designed to provide personalized information based on user resumes. It leverages cutting-edge technologies such as Groq and Hugging Face embeddings, along with FAISS (Facebook AI Similarity Search), to enhance its functionality. Jarvis offers intelligent responses tailored to individual profiles.",
            "link": "https://github.com/yourusername/Chat-Kirtan"
        }
    ]

    html_code = """
        <style>
        .projects-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center; /* Center align items */
        }
        .project-card {
            width: 700px; /* Fixed width for consistent card size */
            margin: 10px;
            padding: 20px;
            background-color: #f0f0f0; /* Light gray background */
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Soft shadow */
            transition: transform 1s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .project-card:hover {
            transform: translateY(-5px); /* Lift card on hover */
            box-shadow: 0 6px 12px rgba(0,0,0,0.15); /* Increased shadow on hover */
            cursor: pointer; /* Change cursor on hover */
        }
        .project-card h2 {
            font-size: 24px;
            margin-bottom: 10px;
            color: #333;
        }
        .project-card p {
            font-size: 16px;
            line-height: 1.5;
            color: #666;
        }
        .project-link {
            display: inline-block;
            margin-top: 10px;
            color: #007bff; /* Blue link color */
            text-decoration: none;
        }
        .project-link:hover {
            text-decoration: underline; /* Underline link on hover */
        }
        .dot-container {
            text-align: center;
            margin-top: 20px;
            margin-bottom: 1px;
        }
        .dot {
            height: 10px;
            width: 10px;
            margin: 0 5px;
            background-color: #999;
            border-radius: 50%;
            display: inline-block;
            cursor: pointer; /* Change cursor to pointer */
            transition: background-color 0.3s ease-in-out;
        }
        .active {
            background-color: #333;
        }
        </style>
        <div class="projects-container">
    """

    for index, project in enumerate(projects):
        if project['title'] == "👁️ ExamEye":
            project_card = f"""
                <div class="project-card" onclick="stopAutoSlide()">
                    <h2>{project['title']}</h2>
                    <p>{project['description']}</p>
                    <a class="project-link" href="{project['link']}" target="_blank">Demo</a>
                </div>
            """ 
            html_code += project_card
        
        else:
            project_card = f"""
                <div class="project-card" onclick="stopAutoSlide()">
                    <h2>{project['title']}</h2>
                    <p>{project['description']}</p>
                    <a class="project-link" href="{project['link']}" target="_blank">GitHub</a>
                </div>
            """ 
            html_code += project_card

    html_code += """
        </div>
        <div class="dot-container">
    """

    for i in range(len(projects)):
        html_code += f'<span class="dot" onclick="currentSlide({i+1})"></span>'

    html_code += """
        </div>
        <script>
        let slideIndex = 0;
        let autoSlide = true; // Variable to control auto slide

        showSlides();

        function showSlides() {
            let i;
            let slides = document.getElementsByClassName("project-card");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            slideIndex++;
            if (slideIndex > slides.length) {slideIndex = 1}    
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            if (autoSlide) {
                setTimeout(showSlides, 10000); // Change slide every 10 seconds
            }
        }

        function currentSlide(n) {
            slideIndex = n-1;
            showSlides();
        }

        function stopAutoSlide() {
            autoSlide = false; // Stop auto slide when clicking on a project card
        }

        // Remove iframes from the HTML to prevent unwanted space
        document.querySelectorAll('iframe').forEach(e => e.remove());
        </script>
    """

    st.components.v1.html(html_code, height=320)

