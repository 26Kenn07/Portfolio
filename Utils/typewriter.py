import streamlit as st

def type_writer():
    st.markdown("""
    <style>

    /* Typewriter effect 1 */
    @keyframes typing {
    0.0000%, 30.3488% { content: ""; }
    1.1395%, 29.2093% { content: "K"; }
    2.2791%, 28.0698% { content: "Ki"; }
    3.4186%, 27.9302% { content: "Kir"; }
    4.5581%, 26.7907% { content: "Kirt"; }
    5.6977%, 25.6512% { content: "Kirta"; }
    6.8372%, 24.5116% { content: "Kirtan"; }
    7.9767%, 23.3721% { content: "Kirtan "; }
    9.1163%, 22.2326% { content: "Kirtan M"; }
    10.2558%, 21.0930% { content: "Kirtan Ma"; }
    11.2558%, 20.0930% { content: "Kirtan Mat"; }
    12.2558%, 19.0930% { content: "Kirtan Mata"; }
    13.2558%, 18.0930% { content: "Kirtan Matal"; }
    14.2558%, 17.0930% { content: "Kirtan Matali"; }
    15.2558%, 16.0930% { content: "Kirtan Matalia"; }
    16.2558%, 16.0930% { content: "Kirtan Matalia."; }

    30.7674%, 60.2791% { content: ""; }
    31.9070%, 59.1395% { content: "a"; }
    33.0465%, 58.0000% { content: "an"; }
    34.1860%, 57.8605% { content: "an A"; }
    35.3256%, 56.7209% { content: "an AI"; }
    36.4651%, 55.5814% { content: "an AI "; }
    37.6047%, 54.4419% { content: "an AI E"; }
    38.6047%, 53.4419% { content: "an AI En"; }
    39.6047%, 52.4419% { content: "an AI Eng"; }
    40.6047%, 51.4419% { content: "an AI Engi"; }
    41.6047%, 50.4419% { content: "an AI Engin"; }
    42.6047%, 49.4419% { content: "an AI Engine"; }
    43.6047%, 48.4419% { content: "an AI Enginee"; }
    44.6047%, 47.4419% { content: "an AI Engineer"; }
    45.6047%, 46.4419% { content: "an AI Engineer."; }


    60.6977%, 85.2093% { content: ""; }
    61.8372%, 80.0698% { content: "a"; }
    62.9767%, 79.9302% { content: "a "; }
    63.1163%, 78.7907% { content: "a S"; }
    64.2558%, 77.6512% { content: "a St"; }
    65.3953%, 76.5116% { content: "a Stu"; }
    66.5349%, 75.3721% { content: "a Stud"; }
    67.5349%, 74.3721% { content: "a Stude"; }
    68.5349%, 73.3721% { content: "a Studen"; }
    69.5349%, 72.3721% { content: "a Student"; }
    70.5349%, 71.3721% { content: "a Student."; }
    }

    @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
    }

    .typewriter {
    --caret: currentcolor;
    }

    .typewriter::before {
    content: "";
    animation: typing 30.5s infinite;
    }

    .typewriter::after {
    content: "";
    border-right: 1px solid var(--caret);
    animation: blink 0.5s linear infinite;
    }

    @media (prefers-reduced-motion) {
    .typewriter::after {
        animation: none;
    }
    
    @keyframes sequencePopup {
        0%, 100% { content: "Kirtan Matalia"; }
        50% { content: "an AI Engineer"; }
        80% { content: "a Student"; }
    }

    .typewriter::before {
        content: "developer";
        animation: sequencePopup 12s linear infinite;
    }
    }
    </style>

    <h1 aria-label="Hi! I'm Kirtan Matalia">
    👋🏻 Hi! I'm&nbsp;<span class="typewriter"></span>
    </h1>
    """, unsafe_allow_html=True)