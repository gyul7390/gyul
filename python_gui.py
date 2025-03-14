import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#만약에 웹브라우저 종료하면 아래 터미널에 
# 1. cd 'C:\Users\Gyul hee\Documents\Ecole\data_anlyst\wildcodeschool\streamlit\test_streamlit'  
# 2. streamlit run python_gui.py입력하기
# 3. (기억을 더듬어서... 네 github에 코드 업로드해서 실행시켜보기)

st.title('Hello, welcome to my dashboard for car!')

st.write('You can descover streamlit.')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

st.write(df)

# 🌎 지역 필터 버튼
region = st.radio("Sélectionnez une région :", ["Toutes", "USA", "Europe", "Japon"])

# 🏎️ 필터 적용
if region == "USA":
    df = df[df["continent"] == "usa"]
elif region == "Europe":
    df = df[df["continent"] == "europe"]
elif region == "Japon":
    df = df[df["continent"] == "japan"]

# 📊 분포 시각화
st.subheader("Distribution du poids des voitures")
fig, ax = plt.subplots()
sns.histplot(df["mpg"], bins=20, kde=True, ax=ax)
st.pyplot(fig)

df_numeric = df.select_dtypes(include=['number'])

# 🔥 상관관계 분석
st.subheader("Matrice de corrélation")
fig, ax = plt.subplots(figsize=(8,6))
corr_matrix = sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)






