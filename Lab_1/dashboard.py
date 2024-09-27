import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend

# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()

# CSS för att sätta bakgrundsbild
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("C:/Users/saram/Klassprojekt/GitHub/Fullstack_data_sara_mellgren/Lab_1/0_0 (1).webp");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>The teacher Kokchun, who wished he was a famous Youtuber</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Den här dashboarden syftar till att utforska datan i min YouTubekanal.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<p style='color: white;'>Content KPI</p>", unsafe_allow_html=True)
    content_kpi.display_content()

with col2:
    st.markdown("<p style='color: white;'>Views Trend</p>", unsafe_allow_html=True)
    views_graph.display_plot()

if __name__ == "__main__":
    layout()
  