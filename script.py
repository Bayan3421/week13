import streamlit as st
import folium
import json
from folium.plugins import MarkerCluster, Search
from streamlit_folium import st_folium

st.title("Карта с маркерами КазАту")

# Загрузка данных
with open("coordinates.json", "r") as file:   
    locations = json.load(file)

# Создаём словарь для поиска маркеров
marker_dict = {loc["name"]: [loc["latitude"], loc["longitude"]] for loc in locations}

# Базовая карта
m = folium.Map(location=[51.187, 71.410], zoom_start=17)

# Кластер маркеров
marker_cluster = MarkerCluster()

# Добавляем маркеры на карту
for loc in locations:
    marker = folium.Marker(
        location=[loc["latitude"], loc["longitude"]],
        popup=loc["name"],
        tooltip=loc["name"]
    )
    marker_cluster.add_child(marker)

m.add_child(marker_cluster)

# Добавляем функционал поиска
search = Search(
    layer=marker_cluster,
    search_label="name",
    placeholder="Найти маркер...",
    collapsed=False
)
m.add_child(search)

# Боковая панель для выбора маркера
st.sidebar.title("Поиск маркера")
marker_name = st.sidebar.selectbox("Выберите маркер:", [""] + list(marker_dict.keys()))

# Обновляем карту при выборе маркера
if marker_name:
    coordinates = marker_dict[marker_name]
    folium.Marker(
        location=coordinates,
        popup=marker_name,
        tooltip="Выбранный маркер",
        icon=folium.Icon(color="red")
    ).add_to(m)
    m.location = coordinates  # Перемещаем карту на выбранный маркер
    m.zoom_start = 18

# Отображаем карту
st_folium(m, width=725)

