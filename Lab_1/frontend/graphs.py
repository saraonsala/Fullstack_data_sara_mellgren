import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.query_database import QueryDatabase
import pandas as pd
import sqlite3

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.content_view_time").df

    def display_plot(self):
        st.markdown("## Kokchuns topp 10 Videor")

        # Sortera efter de 10 populäraste videorna
        top_videos = self.df.nlargest(10, "Visningar")

        # Skapa linjediagram med Plotly
        fig = px.line(top_videos, x="Videotitel", y="Visningar", title="Antal visningar per video", markers=True)

        # Visa grafen i Streamlit
        st.plotly_chart(fig, use_container_width=True)


class DeviceDate:
    
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_views_date;").df

    def display_plot(self):
        # Visa nya visualiseringar
        st.subheader("Enhetsvyer över tid")
        device_views_date_df = self.df
        fig_views_date = px.line(device_views_date_df, x='Datum', y='Visningar', color='Enhetstyp', title='Visningar per Enhetstyp över Tid')
        fig_views_date.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_views_date, use_container_width=True)

class DeviceSummary:
    
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_summary;").df
        
    def display_plot(self):
        st.subheader("Sammanfattning av enhetstyper")
        device_summary_df= self.df
        fig_summary = px.bar(device_summary_df, x='Enhetstyp', y='Visningar', title='Sammanfattning av Visningar per Enhetstyp')
        fig_summary.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_summary, use_container_width=True)

        st.subheader("Genomsnittlig visningstid per enhet")
        fig_avg_watch_time = px.bar(device_summary_df, x='Enhetstyp', y='Visningslängd_genomsnitt', title='Genomsnittlig Visningslängd per Enhetstyp')
        fig_avg_watch_time.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_avg_watch_time, use_container_width=True)

        st.subheader("Total visningstid per enhet")
        fig_total_watch_time = px.bar(device_summary_df, x='Enhetstyp', y='Visningstid_timmar', title='Total Visningstid (timmar) per Enhetstyp')
        fig_total_watch_time.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_total_watch_time, use_container_width=True)

