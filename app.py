import streamlit as st
import streamlit.components.v1 as components

# Embed the iframe with custom styling
st.write(
    """
    <style>
    .custom-iframe {
        height: 800px; /* Adjust height as needed */
        width: 150%; /* Stretch iframe horizontally */
        border: none;
        display: block;
        margin: 0 auto;
        margin-left: center; /* Center iframe horizontally */
        margin-right: auto; /* Center iframe horizontally */
       
    }
    .custom-iframe #GithubIcon {
        display: none; /* Hide the GitHub icon */
        visibility: hidden;
    }
    
    </style>
    <iframe class="custom-iframe" allow="web-share; fullscreen" src="https://amuselabs.com/pmm/crossword?id=109e269b&set=38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8&embed=1" aria-label="Puzzle Me Game"> </iframe>
    """,
    unsafe_allow_html=True
)



