import streamlit as st

pages = {
    "Your account": [
        st.Page("despesas.py", title="DashBoard"),
        st.Page("cotacao.py", title="Cotação Euro"),
    ],
}

pg = st.navigation(pages)
pg.run()
