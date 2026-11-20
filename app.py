import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Агрометеорологический агент", page_icon="🌾")

# Логотип
try:
    logo = Image.open("фронт.jpg")
    st.image(logo, width=200)
except:
    st.write("Логотип не найден")

st.title("🌾 Агрометеорологический агент")
st.write("Введите координаты, чтобы получить прогноз и рекомендации.")

lat = st.number_input("Широта (lat)", value=55.75, format="%.4f")
lon = st.number_input("Долгота (lon)", value=37.62, format="%.4f")
farm_name = st.text_input("Название хозяйства", "СПК Рассвет")
crop = st.text_input("Культура", "Озимая пшеница")

if st.button("Получить бюллетень"):
    with st.spinner("Запрашиваем данные..."):
        url = f"https://webhook.nodul.ru/28657/prod/3a93f2b4-c2f7-47a1-a808-9d9668975aa9?lat={lat}&lon={lon}&farm_name={farm_name}&crop={crop}&stage=Кущение"
        
        try:
            response = requests.get(url, headers={"Expect": ""})
            if response.status_code == 200:
                data = response.json()
                st.success("Данные получены!")
                
                st.subheader("📝 Бюллетень")
                st.info(data.get("bulletin_text", "Текст не найден"))
                
                st.subheader("⚠️ Риски")
                st.json(data.get("risks", []))
            else:
                st.error(f"Ошибка: {response.status_code}")
        except Exception as e:
            st.error(f"Ошибка подключения: {e}")

# Копирайт
st.markdown("---")
st.caption("ГК Юзтех © 2026")
