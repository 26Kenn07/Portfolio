import streamlit as st

def show_projects():
    st.header("🛠️ Projects")
    
    # Initialize session state
    if 'is_phone' not in st.session_state:
        st.session_state.is_phone = False
    
    projects = [
        {
            "title": "👁️ ExamEye",
            "description": "It is an AI guardian for secure online exams, offering real-time vigilance, smart anti-cheating measures.",
            "link": "https://drive.google.com/file/d/1kPd9Cv4LrqeUHABiJcU-8ZcBEC5tH20S/view"
        },
        {
            "title": "🏏 Sports Action Detection",
            "description": "Created and curated diverse datasets and YOLOv8 model with 1000+ images of sports actions.",
            "link": "https://github.com/26Kenn07/Sports_Action_Detection_Using_YOLO"
        },
        {
            "title": "🤖 Jarvis",
            "description": "Jarvis is an advanced chatbot assistant designed to provide personalized information based on user documents.",
            "link": "#"
        }
    ]

    html_code = """
        <style>
        .projects-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .project-card {
            flex: 1 1 calc(33% - 20px); /* Adjust the flex-basis to make it responsive */
            margin: 10px;
            padding: 20px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            cursor: pointer;
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
            color: #007bff;
            text-decoration: none;
        }
        .project-link:hover {
            text-decoration: underline;
        }
        .dot-container {
            text-align: center;
            margin-top: 20px;
        }
        .dot {
            height: 10px;
            width: 10px;
            margin: 0 5px;
            background-color: #999;
            border-radius: 50%;
            display: inline-block;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }
        .active {
            background-color: #333;
        }
        @media (max-width: 1200px) {
            .project-card {
                flex: 1 1 calc(50% - 20px); /* Two columns on medium screens */
            }
        }
        @media (max-width: 768px) {
            .project-card {
                flex: 1 1 100%; /* Single column on small screens */
            }
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.4);
            padding-top: 60px;
        }
        .modal-content {
            background-color: #fefefe;
            margin: 5% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
        }
        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
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
        
        elif project['title'] == "🤖 Jarvis":
            project_card = f"""
                <div class="project-card" onclick="stopAutoSlide()">
                    <h2>{project['title']}</h2>
                    <p>{project['description']}</p>
                    <a class="project-link" href="javascript:void(0);" onclick="openModal()">Chat With Jarvis</a>
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
        <div id="myModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal()">&times;</span>
                <h2>Chat with Jarvis</h2>
                <p>You can chat with Jarvis by scrolling down to the Jrvis section.</p>
                <!-- Here you can add an iframe or any other content to represent the chatbot interface -->
            </div>
        </div>
        <script>
        let slideIndex = 0;
        let autoSlide = true;

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
                setTimeout(showSlides, 10000); 
            }
        }

        function currentSlide(n) {
            slideIndex = n-1;
            showSlides();
        }

        function stopAutoSlide() {
            autoSlide = false;
        }

        function openModal() {
            document.getElementById("myModal").style.display = "block";
        }

        function closeModal() {
            document.getElementById("myModal").style.display = "none";
        }

        document.querySelectorAll('iframe').forEach(e => e.remove());

        // Adjust height based on user's screen size
        function adjustHeight() {
            let availableHeight = window.innerHeight;
            let componentHeight;
            if (window.innerWidth <= 768) {
                componentHeight = Math.max(1200, availableHeight - 200); // Minimum height of 1200px for phone
                window.parent.streamlitSessionState.set('is_phone', true);
            } else {
                componentHeight = Math.max(350, availableHeight - 200); // Minimum height of 350px for computer
                window.parent.streamlitSessionState.set('is_phone', false);
            }
            let htmlComponents = document.getElementsByClassName('streamlit-component-html');
            for (let i = 0; i < htmlComponents.length; i++) {
                htmlComponents[i].style.height = componentHeight + 'px';
            }
        }

        window.addEventListener('resize', adjustHeight);
        adjustHeight(); // Initial adjustment on page load
        </script>
    """

    # Set the initial height based on the session state
    initial_height = 1200 if st.session_state.is_phone else 350
    st.components.v1.html(html_code, height=initial_height)

