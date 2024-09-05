import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[1] / "../data"
    df = pd.read_csv(data_path /"cleaned_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df


def layout():
    df = read_data()
    # to fix streamlits comma for thousands
    df_reset = df.reset_index(names=["year"]).style.format({"year": lambda x: f"{x}"}) # f"{x:,}"}) detta retonerar X men utan komma
    st.markdown("# YH dashboard")

    st.markdown("This is a simple dashboard about yrkeshögskola")
    st.markdown("Sara är bäst!")

    st.markdown("## Raw data")
    st.markdown("This data shows number of started educations per region and per year")
    st.dataframe(df_reset)

    st.markdown("## Trends per region") ##är en underrubrik i markdown
    region = st.selectbox("Choose region", df.columns) # df.columns = alla kolumner i df #skapar en dropdown meny

    region_stats = df[region].describe()
    cols = st.columns(4)
    stats = ["min", "50%", "max"]
    labels = ["min", "median", "max"]
    for col, stat, label in zip(cols, stats, labels):
        with col:
            st.metric(label=label, value=f"{region_stats[stat]:.0f}")

    fig = px.line(
        data_frame=df,
        x=df.index,
        y=df[region],
        title=f"started educations in {region} 2007-2023",
        labels={"index": "year", region: "started educations"},
    )
    fig.update_traces(line=dict(width=3))
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig)
    
def read_css():
    css_path = Path(__file__).parents[1] / "style.css"
    
    with open("style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


if __name__ == "__main__": #__name__ är en specialvariabel som är satt till namnet på modulen som körts. Om modulen är huvudmodulen är __name__ satt till __main__.
    # print(read_data())
    layout()
