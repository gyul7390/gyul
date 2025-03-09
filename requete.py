import streamlit as st
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
from streamlit_authenticator import Authenticate

#만약에 웹브라우저 종료하면 아래 터미널에 
# 1. cd 'C:\Users\Gyul hee\Documents\Ecole\data_anlyst\wildcodeschool\streamlit\test_streamlit'  
# 2. streamlit run requete.py입력하기


import streamlit as st
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': 
    {'utilisateur': 
    {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate( #인증 객체 생성
    lesDonneesDesComptes, # Les données des comptes # 사용자 계정 정보
    "cookie name", # Le nom du cookie, un str quelconque 쿠키 이름 (아무 문자열)
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 쿠키 만료 기간(일)
) 

# ✅ 로그인 전일 때만 ID/Password 문구 표시
if "authentication_status" not in st.session_state or st.session_state["authentication_status"] is None:
    st.title("ID : root / Password : rootMDP")

# 로그인 화면 표시
authenticator.login()

if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        selection = option_menu(   
            menu_title=f"Bienvenue root",
            options=["Accueil", "Photos"],
            icons=["house", "camera"]
        )

    # ✅ 선택한 메뉴에 따라 화면 표시
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
        st.image("https://gratisography.com/wp-content/uploads/2025/01/gratisography-dog-vacation-1170x780.jpg")
    elif selection == "Photos":
        st.title("Bienvenue dans l'album de chien !!!")
        col1, col2, col3 = st.columns(3)

        with col1:
          st.header("A muffin")
          st.image("https://www.topbots.com/downloads/code/vision/chihuahua_vs_muffin/test1.png")

        with col2:
           st.header("A dog")
           st.image("https://www.topbots.com/downloads/code/vision/chihuahua_vs_muffin/test12.png")

        with col3:
          st.header("A dog")
          st.image("https://www.topbots.com/downloads/code/vision/chihuahua_vs_muffin/test2.png")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
