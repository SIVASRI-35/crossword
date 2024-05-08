import streamlit as st

#import streamlit as st

# Hide GitHub icon CSS
hide_github_icon = """
<style>
#GithubIcon { 
    visibility: hidden;
}
</style>
"""


iframe_code = """
<iframe height="700px" width="100%" allow="web-share; fullscreen" style="border:none; width: 100% !important; position: static;display: block !important; margin: 0 !important;" src="https://amuselabs.com/pmm/crossword?id=109e269b&set=38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8&embed=1" aria-label="Puzzle Me Game"></iframe>
"""

st.components.html(iframe_code)
