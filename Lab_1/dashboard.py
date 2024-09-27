import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()


def layout():
    # Anpassad CSS-stil för att göra dashboarden mer attraktiv
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #ff6347;
        text-align: center;
    }
    .section-title {
        color: #4B0082;
        font-size: 24px;
        font-weight: bold;
    }
    .description {
        color: #808080;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # Huvudrubrik
    st.markdown("<h1>The teacher Kokchun, who wished he was a famous Youtuber</h1>", unsafe_allow_html=True)
    
    # Introduktionstext
    st.markdown("<p class='description'>Den här dashboarden syftar till att utforska datan i hans YouTubekanal.</p>", unsafe_allow_html=True)
    
    # Dela upp layouten i två kolumner med lika stor bredd
    col1, col2 = st.columns([1, 1])

# I den första kolumnen kan vi visa KPI:er och innehållsrelaterad data
    with col1:
        st.markdown("<p class='section-title'>Content KPI</p>", unsafe_allow_html=True)
        content_kpi.display_content()

# I den andra kolumnen kan vi visa grafer eller annan information
    with col2:
        st.markdown("<p class='section-title'>Views Trend</p>", unsafe_allow_html=True)
        views_graph.display_plot()

    # Lägg till en trevlig bild för att göra det visuellt intressantare
    st.image("https://source.unsplash.com/random/800x400", caption="Din YouTube-resa visualiserad", use_column_width=True)

if __name__ == "__main__":
    layout()