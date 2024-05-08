import streamlit as st
import streamlit.components.v1 as components



# Define CSS to hide GitHub icon and prevent wrapping of the iframe content
css_code = """
<style>
#GithubIcon { 
    visibility: hidden;
}
iframe {
    white-space: nowrap;
}
</style>
"""

# Define the iframe code with increased height
iframe_code = """
<iframe height="5000px" width="500%" allow="web-share; fullscreen" style="border:none; width: 100% !important; position: static;display: block !important; margin: 0 !important;" src="https://amuselabs.com/pmm/crossword?id=109e269b&set=38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8&embed=1" aria-label="Puzzle Me Game"></iframe>
"""

# Combine CSS and iframe code and display using components.html()
components.html(css_code + iframe_code)


