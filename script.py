import streamlit as st
import folium
import json
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium


st.title("Карта с маркерами")


with open("coordinates.json", "r") as file:
    locations = json.load(file)


m = folium.Map(location=[51.187, 71.410], zoom_start=17)


marker_cluster = MarkerCluster()


for loc in locations:
    marker = folium.Marker(
        location=[loc["latitude"], loc["longitude"]],
        popup=loc["name"],
        tooltip=loc["name"]
    )
    marker_cluster.add_child(marker)

m.add_child(marker_cluster)


st_folium(m, width=725)
