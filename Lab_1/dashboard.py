import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend
import plotly.express as px
import pandas as pd
import sqlite3
from frontend.graphs import DeviceDate
from frontend.graphs import DeviceSummary


content_kpi = ContentKPI()
views_graph = ViewsTrend()
device_views_date_df = DeviceDate()
device_summary_df = DeviceSummary()


# CSS för att sätta bakgrundsbild
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.saramellgren.com/wp-content/uploads/2023/11/saram0214_an_astronaut_playing_with_jellyfish_fa601ffe-ecda-4a23-9977-f958ecb739e4-1.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def layout():
    st.markdown("# Code by day, viral by night – the teacher who swapped bugs for subscribers")
    st.markdown("Den här dashboarden syftar till att utforska datan i min lärare Kokchuns youtubekanal")
    content_kpi.display_content()
    views_graph.display_plot()
    device_views_date_df.display_plot()
    device_summary_df.display_plot()
    

if __name__ == "__main__":
    layout()
    