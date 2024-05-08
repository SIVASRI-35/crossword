import streamlit as st
import streamlit.components.v1 as components



# Define CSS to hide GitHub icon
hide_github_icon = """
<style>
#GithubIcon { 
    visibility: hidden;
}
</style>
"""

# Define the iframe code with height set to 100vh
iframe_code = """
<iframe height="100vh" width="500%" allow="web-share; fullscreen" style="border:none; width: 100% ; !important; !important;" src="https://amuselabs.com/pmm/crossword?id=109e269b&set=38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8&embed=1" aria-label="Puzzle Me Game"></iframe>
"""

# Combine CSS and iframe code and display using components.html()
components.html(hide_github_icon + iframe_code)


