import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase


# ViewsTrend klassen
    # class ViewsTrend:
    #     def __init__(self) -> None:
    #         self.df = QueryDatabase("SELECT * FROM marts.views_trend").df

    #     def display_plot(self):
    #         st.markdown("## Visningstrend")
    #         # Skapa en linjediagram för visningstrend
    #         fig, ax = plt.subplots()
    #         ax.plot(self.df["Datum"], self.df["Visningar"], marker="o", color="r")
    #         ax.set_title("Visningstrend")
    #         ax.set_xlabel("Datum")
    #         ax.set_ylabel("Visningar")
    #         ax.grid(True)
    #         st.pyplot(fig)




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
