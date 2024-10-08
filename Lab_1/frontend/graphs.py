import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase

# GenderTrend klassen
class GenderTrend:
    def __init__(self) -> None:
        # Hämta data från databasen
        self.df = QueryDatabase("SELECT * FROM marts.gender_trend").df
        
    def display_plot(self):
        st.markdown("## Könsfördelning av mina videor")

        # Gruppera datan för att summera antalet tittare per kön
        gender_counts = self.df.groupby("Tittarnas kön").size().reset_index(name="Antal Tittare")

        # Skapa ett cirkeldiagram för könsfördelning
        fig = px.pie(gender_counts, names="Tittarnas kön", values="Antal Tittare", 
                     title="Könsfördelning av Tittare")

        # Lägg till interaktivitet och stilinställningar
        fig.update_traces(textinfo="percent+label", hoverinfo="label+percent+value")
        fig.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        
        # Visa grafen
        st.plotly_chart(fig)

# Skapa en instans av klassen och visa diagrammet
#gender_trend = GenderTrend()
#gender_trend.display_plot()




# VideosTitle klassen
class VideosTitle:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.videos_title").df

    def display_plot(self):
        st.markdown("## Videovisningar efter Titel")
        # Sortera efter populäraste videorna
        top_videos = self.df.largest(10, "Visningar")

        # Visa i en tabell
        st.table(top_videos[["Titel", "Visningar"]])
