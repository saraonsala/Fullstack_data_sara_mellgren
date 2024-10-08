import streamlit as st
from utils.query_database import QueryDatabase
import pandas as pd

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för Kokchuns olika videos📹")
        st.markdown("### Totalt antal")

        # Skapa en drop down meny för att välja en specifik video
        video_titles = df["Videotitel"].unique()
        selected_video = st.selectbox("Välj en video", video_titles)

        # Filtrera data baserat på det valda videon
        filtered_df = df[df["Videotitel"] == selected_video]

        kpis = {
            "Antal videor": len(filtered_df),
            "Totalt visade timmar": filtered_df["Visningstid_timmar"].sum(),
            "Totalt antal prenumeranter": filtered_df["Prenumeranter"].sum(),
            "Totalt antal exponeringar": filtered_df["Exponeringar"].sum(),
        }

        # Använd olika färger för att framhäva KPI:er
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📹 Videor", kpis["Antal videor"], delta_color="inverse")
        col2.metric("⏱️ Visade timmar", round(kpis["Totalt visade timmar"], 1), delta_color="normal")
        col3.metric("👤 Prenumeranter", round(kpis["Totalt antal prenumeranter"]), delta_color="normal")
        col4.metric("👁️ Exponeringar", round(kpis["Totalt antal exponeringar"]), delta_color="normal")

        # Visualisera data som tabell
        st.markdown("### Videotitlar")
        st.dataframe(filtered_df)

       
        # Diagram över datan
        st.markdown("### Antal tittade minuter per video")
        st.bar_chart(filtered_df[["Visningstid_timmar"]])




            
    

#device_kpi()
    
    


