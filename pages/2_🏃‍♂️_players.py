import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_state = df_data[df_data["Name"] == player].iloc[0]

st.image(player_state["Photo"])
st.title(player_state["Name"])

st.markdown(f"**Clube:** {player_state['Club']}")
st.markdown(f"**Posição:** {player_state['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_state['Age']}")
col2.markdown(f"**Altura:** {player_state['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_state['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_state['Overall']}")
st.progress(int(player_state["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£ {player_state['Value(£)']:,}")
col2.metric(label="Remuneração Semanal", value=f"£ {player_state['Wage(£)']:,}")
col3.metric(label="Cláusula de Recisão", value=f"£ {player_state['Release Clause(£)']:,}")

