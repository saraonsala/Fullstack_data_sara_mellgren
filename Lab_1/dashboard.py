import streamlit as st 
from frontend.kpi import ContentKPI
#from frontend.graphs import ViewsTrend
from frontend.graphs import GenderTrend

#device_kpi = DeviceKPI() 
content_kpi = ContentKPI()
#views_graph = ViewsTrend()
gender_trend = GenderTrend()


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
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    #views_graph.display_plot()
    gender_trend.display_plot()
    
    
  


if __name__ == "__main__":
    layout()
    