import streamlit as st

st.set_page_config(page_title="Portal de Apps", layout="wide")
st.title("🔎 Portal de Aplicativos")
st.write("Clique em um aplicativo para abrir em uma nova aba.")

APPS = [
    {
        "name": "Função Degrau",
        "desc": "Ajuste e visualização de curvas com degraus.",
        "icon": "assets/degrau.png",
        "url": "https://ajustedefuncaodegrau.streamlit.app",
        "github": "https://github.com/MarioNunes35/Fun-o-degrau/blob/main/degrau.py",
    },
    {
        "name": "Ajuste de Eixo e de Tempo",
        "desc": "Corrige deslocamentos de eixo e tempo em séries.",
        "icon": "assets/eixo_tempo.png",
        "url": "https://ajustedeeixo.streamlit.app",
        "github": "https://github.com/MarioNunes35/Ajuste-de-eixo-e-de-tempo/blob/f7add251a4ed88a0f6be680dc31e8545b6763012/ajustedeeixo.py",
    },
    {
        "name": "Conversor de Tempo",
        "desc": "Converte formatos mm:ss ↔ s com utilitários práticos.",
        "icon": "assets/tempo.png",
        "url": "https://conversordetempo.streamlit.app",
        "github": "https://github.com/MarioNunes35/conversordetempo/blob/main/conversor-de-tempo.py",
    },
    {
        "name": "Conversor nm → bar",
        "desc": "Converte leituras em nm para bar (calibração).",
        "icon": "assets/nm_bar.png",
        "url": "https://conversor-de-nm-para-bar.streamlit.app",
        "github": "https://github.com/MarioNunes35/Conversor-de-nm-para-bar/blob/main/conversor-de-nm-para-bar.py",
    },
]

cols = st.columns(3, gap="large")

def card(app, col):
    with col:
        st.image(app["icon"], use_container_width=True)
        st.markdown(f"### {app['name']}")
        st.caption(app["desc"])
        st.link_button("Abrir", app["url"], use_container_width=True)
        st.markdown(f"[Código-fonte]({app['github']})")

for i, app in enumerate(APPS):
    card(app, cols[i % 3])
