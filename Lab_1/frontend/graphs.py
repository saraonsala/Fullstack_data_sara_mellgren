import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase

# GenderTrend klassen
class GenderTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.gender_trend").df  # Uppdatera SQL-frågan för att inkludera könsdata

    def display_plot(self):
        # Filtrera efter kön med dropdown (lägg till unikt key)
        gender_filter = st.selectbox("Välj kön", ["Man", "Kvinna"], key="gender_filter")
        
        # Filtrering baserat på kön
        if gender_filter != "Alla":
            filtered_df = self.df[self.df['Tittarnas kön'] == gender_filter]
        else:
            filtered_df = self.df

        # Skapa data för Matplotlib
        x = filtered_df['Tittarnas ålder'].unique()
        y = filtered_df.groupby('Tittarnas ålder')['Visningstid (timmar) (%)'].sum()

        # Skapa stapeldiagram med Matplotlib
        fig, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        ax.set(xlim=(min(x)-1, max(x)+1), xticks=np.arange(min(x), max(x)+1),
               ylim=(0, max(y)+1), yticks=np.arange(0, max(y)+1))

                



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



