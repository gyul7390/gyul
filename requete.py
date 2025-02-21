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

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
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

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes # 사용자 계정 정보
    "cookie name", # Le nom du cookie, un str quelconque 쿠키 이름 (아무 문자열)
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
) 

authenticator.login() # 로그인 폼 표시

def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés") # 로그인한 사용자만 볼 수 있는 화면



if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    
    
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
# ... et ainsi de suite pour les autres pages