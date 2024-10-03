from utils.query_database import QueryDatabase 
import plotly.express as px
import streamlit as st

# Skapa en sidotitel och layout
st.set_page_config(page_title="Dashboard för Videodata", layout="wide")
st.title("Analys av Videovisningar och Könsfördelning")

# ViewsTrend klassen
class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df

    def display_plot(self):
        # Dropdown för att filtrera datum (lägg till unikt key)
        date_range = st.selectbox("Välj tidsperiod", ["Senaste månaden", "Senaste året", "Alla"], key="views_date_range")
        
        # Filtrering baserat på val
        if date_range == "Senaste månaden":
            filtered_df = self.df[self.df["Datum"] >= "2024-09-01"]
        elif date_range == "Senaste året":
            filtered_df = self.df[self.df["Datum"] >= "2023-10-01"]
        else:
            filtered_df = self.df
        
        # Plot med Plotly
        fig = px.line(filtered_df, x="Datum", y="Visningar", title="Antal Visningar över Tid")
        fig.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')
        
        # Visa grafen
        st.plotly_chart(fig, use_container_width=True)

# GenderTrend klassen
class GenderTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.gender_views").df  # Uppdatera SQL-frågan för att inkludera könsdata

    def display_plot(self):
        # Filtrera efter kön med dropdown (lägg till unikt key)
        gender_filter = st.selectbox("Välj kön", ["Alla", "Man", "Kvinna", "Övrigt"], key="gender_filter")
        
        # Filtrering baserat på kön
        if gender_filter != "Alla":
            filtered_df = self.df[self.df["Kön"] == gender_filter]
        else:
            filtered_df = self.df

        # Skapa linjediagram med Plotly
        fig = px.line(filtered_df, x="Datum", y="Visningar", color="Kön", title="Visningar per Kön över Tid")
        fig.update_layout(autosize=True, plot_bgcolor='rgba(0,0,0,0)')

        # Visa grafen
        st.plotly_chart(fig, use_container_width=True)

# VideosTitle klassen
class VideosTitle:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.videos_title").df

    def display_plot(self):
        st.markdown("## Videovisningar efter Titel")
        # Sortera efter populäraste videorna
        top_videos = self.df.nlargest(10, "Visningar")

        # Visa i en tabell
        st.table(top_videos[["Titel", "Visningar"]])

# Anropa funktionerna och visa i layout med två kolumner
with st.sidebar:
    st.header("Filtreringsalternativ")
    view_type = st.radio("Välj datatyp", ["Visningar över tid", "Visningar per kön", "Videotitlar"], key="view_type_radio")

# Layout för huvudsektionen
if view_type == "Visningar över tid":
    with st.container():
        ViewsTrend().display_plot()

elif view_type == "Visningar per kön":
    with st.container():
        GenderTrend().display_plot()

else:
    with st.container():
        VideosTitle().display_plot()

