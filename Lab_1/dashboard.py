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

st.markdown("<h1 style='text-align: center; color: white;'>The teacher Kokchun, who wished he was a famous Youtuber</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Den här dashboarden syftar till att utforska datan i min YouTubekanal.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<p style='color: white;'>Content KPI</p>", unsafe_allow_html=True)
    content_kpi.display_content()

with col2:
    st.markdown("<p style='color: white;'>Views Trend</p>", unsafe_allow_html=True)
    views_graph.display_plot()

def layout():
    st.markdown("<p style='color: white;'>This is the layout function.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    layout()
  