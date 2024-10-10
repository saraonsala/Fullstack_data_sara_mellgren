import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase


class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.content_view_time").df

    def display_plot(self):
        st.markdown("## Visningstrend för Topp 10 Videor")

        # Sortera efter de 10 populäraste videorna
        top_videos = self.df.nlargest(10, "Visningar")

                # Skapa linjediagram med Plotly
        fig = px.line(top_videos, x="Videotitel", y="Visningar", title="Visningstid för Topp 10 Videor", markers=True)

        # Visa grafen i Streamlit
        st.plotly_chart(fig, use_container_width=True)
