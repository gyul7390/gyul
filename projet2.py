import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

selection = option_menu(   
            menu_title=f"Bienvenue !",
            options=["Accueil", "Recommandations de films"],
            icons=["house", "camera"])
                   
if selection == "Accueil":
        st.title('Welcome to the website recommend the movie')
        st.write("How about new movie ?")
        st.image("main.jpg", caption = 'Click the image', width=500)
elif selection == "Recommandations de films":
    st.text_input("Quel genre de films aimes-tu ? ")
