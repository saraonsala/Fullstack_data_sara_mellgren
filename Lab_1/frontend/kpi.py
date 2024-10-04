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

    
        kpis = {
            "Antal videor": len(df),
            "Totalt visade timmar": df["Visningstid_timmar"].sum(),
            "Totalt antal prenumeranter": df["Prenumeranter"].sum(),
            "Totalt antal exponeringar": df["Exponeringar"].sum(),
        }

        # Använd olika färger för att framhäva KPI:er
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📹 Videor", kpis["Antal videor"], delta_color="inverse")
        col2.metric("⏱️ Visade timmar", round(kpis["Totalt visade timmar"], 1), delta_color="normal")
        col3.metric("👤 Prenumeranter", round(kpis["Totalt antal prenumeranter"]), delta_color="normal")
        col4.metric("👁️ Exponeringar", round(kpis["Totalt antal exponeringar"]), delta_color="normal")

        # Visualisera data som tabell
        st.markdown("### Videotitlar")
        st.dataframe(df)

        # Diagram över datan
        st.markdown("### Antal tittade minuter per video")
        st.bar_chart(df[["Visningstid_timmar"]])




            
    

#device_kpi()
    
    


