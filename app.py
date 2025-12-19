# Streamlit applicaton
import streamlit as st
from utils import StockAPI

st.set_page_config(page_title="Stock Market App", layout="wide")


@st.cache_resource()
def get_stock_api():
    return StockAPI()


stock_api = get_stock_api()


@st.cache_data(ttl=3600)
def search_stock(company: str):
    return stock_api.search_symbol(company)


@st.cache_data(ttl=3600)
def daily_data(symbol: str):
    return stock_api.get_daily_data(symbol)


@st.cache_data(ttl=3600)
def plot_chart(df):
    return stock_api.plot_chart(df)


# Add the title
st.title("Stock Market App")
st.subheader("by Utkarsh Gaikwad")

# Add the text input for company name
company = st.text_input("Company name :")

# Search symbol
if company:
    search = search_stock(company)
    st.dataframe(search)
    sel_symbol = st.selectbox(label="Select stock symbol", options=search)

    if st.button("Plot Chart"):
        df = daily_data(sel_symbol)
        st.dataframe(df.head())
        chart = plot_chart(df)
        st.plotly_chart(chart)
