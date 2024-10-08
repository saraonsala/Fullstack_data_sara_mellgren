import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase
#        

# GenderTrend klassen
class GenderTrend:
    def __init__(self) -> None:
        # Hämta data från databasen
        self.df = QueryDatabase("SELECT * FROM marts.gender_trend").df
        
    def display_plot(self):
        st.markdown("## Skillnaden mellan män och kvinnor som tittar på mina videor")   

        # Skapa linjediagram med befintliga kolumner
        fig = px.line(self.df, x="Tittarnas ålder", y="Tittarnas kön", color="Tittarnas kön", title="Visningar per Kön och Ålder")
        fig.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        # Visa grafen
        st.plotly_chart(fig)




# VideosTitle klassen
class VideosTitle:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.videos_title").df

    def display_plot(self):
        st.markdown("## Videovisningar efter Titel")
        # Sortera efter populäraste videorna
        top_videos = self.df.nlargest(10, "Visningar")

        # Visa i en tabell
        st.table(top_videos[["Titel", "Visningar"]])
