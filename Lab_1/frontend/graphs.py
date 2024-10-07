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
        print(self.df.head())  # Kontrollera datan

    def display_plot(self):
        # Dropdown för att välja kön
        gender_filter = st.selectbox("Välj kön", ["Man", "Kvinna"], key="gender_filter")

        # Filtrera efter kön
        if gender_filter != "Alla":
            filtered_df = self.df[self.df["Tittarnas kon"].str.lower() == gender_filter.lower()]
        else:
            filtered_df = self.df

        # Skapa linjediagram med befintliga kolumner
        fig = px.line(filtered_df, x="Tittarnas alder", y="Visningar (%)", color="Tittarnas kon", title="Visningar per Kön och Ålder")
        fig.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')

        # Visa grafen
        st.plotly_chart(fig, use_container_width=True)






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



