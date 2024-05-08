import streamlit as st
import streamlit.components.v1 as components


#import streamlit.components.v1 as components

# Define the HTML and JavaScript code
html_code = """
<!-- Include the CryptoJS library for hashing the user id before sending it to the PuzzleMe server. -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
<!-- Include the javascript library for embedding this puzzle. -->
<script id="pm-script" src="https://amuselabs.com/pmm/js/puzzleme-embed.js"></script>
<!-- Specify the Amuse Labs server name from where the puzzles will be served -->
<script>
PM_Config.PM_BasePath = "https://amuselabs.com/pmm/";
</script>
<!-- Specifies the puzzle to be embedded on the page. If you want to render multiple games on your page then you can copy paste it multiple times. -->
<div class="pm-embed-div" data-id="109e269b" data-set="38549d5e35e37b3e5de58138b84c6564ac41d6e667cc86e5733632cc3c3197f8" data-puzzleType="crossword" data-height="700px"></div>
"""

# Render the HTML and JavaScript code using components.html()
components.html(html_code)
