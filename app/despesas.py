import streamlit as st
import pandas as pd
import altair as alt

data = {
    "Nome": ["Ademar", "Julia", "Marcia", "Sofia"],
    "Total": [160, 200, 250, 270],
    "Fev": [100, 150, 200, 250],
    "Mar": [120, 160, 210, 230],
    "Abr": [130, 170, 220, 240],
    "Mai": [140, 180, 230, 250],
    "Jun": [150, 190, 240, 260],
    "Jul": [160, 200, 250, 270],
    "Pago": [160, 200, 250, 270],
}

# Convertendo para DataFrame
df = pd.DataFrame(data)

# Definindo os meses
meses = ["Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Total", "Pago"]

# Mostrando os dados em Streamlit
st.title("Familia Sawczenko")
st.markdown("O objetivo deste site é calcular os gastos mensais com a cidadania polonesa e o valor a ser pago")
st.dataframe(df)

# Reformatando os dados para o gráfico
df_melted = df.melt(id_vars=["Nome"], value_vars=meses, 
                    var_name="Mês", value_name="Valor Pago (R$)")

# Criando o gráfico com Altair
chart = (
    alt.Chart(df_melted)
    .mark_line(point=True)
    .encode(
        x="Mês:T",
        y="Valor Pago (R$):Q",
        color="Nome:N",
        tooltip=["Nome:N", "Mês:T", "Valor Pago (R$):Q"],
    )
    .properties(title="Pagamentos mensais de cada pessoa")
)

# Exibindo o gráfico no Streamlit
st.altair_chart(chart, use_container_width=True)

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
