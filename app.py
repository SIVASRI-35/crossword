import streamlit as st
import streamlit.components.v1 as components





# Define CSS to hide GitHub icon and maximize iframe height
css_code = """
<style>
#GithubIcon { 
    visibility: hidden;
}
iframe {
    height: 100vh; /* 100% of the viewport height */
    width: 100%; /* 100% of the available width */
}
</style>
"""

# Define the iframe code
iframe_code = """
<iframe allow="web-share; fullscreen" style="border:none; width: 100% !important; position: static;display: block !important; margin: 0 !important;" src="https://amuselabs.com/pmm/crossword?id=109e269b&set=38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8&embed=1" aria-label="Puzzle Me Game"></iframe>
"""

# Combine CSS and iframe code and display using components.html()
components.html(css_code + iframe_code)

