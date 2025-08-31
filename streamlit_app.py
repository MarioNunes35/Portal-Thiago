# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Portal de Apps", layout="wide")

# ---------- ESTILO (glass + dark) ----------
st.markdown("""
<style>
.stApp {
  background:
    radial-gradient(1200px 500px at 20% -10%, rgba(99,102,241,0.25), transparent 40%),
    radial-gradient(1000px 450px at 90% 10%, rgba(45,212,191,0.22), transparent 40%),
    linear-gradient(180deg, #121317 0%, #0f1116 100%) !important;
  color: #EAEAF1;
}
.nav { position: sticky; top: 0; z-index: 20; padding: 14px 22px; margin: -1.2rem -1rem 0 -1rem;
  backdrop-filter: blur(8px); background: rgba(255,255,255,0.06);
  border-bottom: 1px solid rgba(255,255,255,0.12); }
.brand { font-weight: 700; font-size: 1.05rem; letter-spacing: .02em; }

.block-container input[type="text"]{
  background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.20);
  border-radius: 999px !important; color: #fff !important;
}
.block-container .stTextInput > div > div{ border-radius: 999px !important; }

.grid{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px; margin-top: 10px; }
.card{ position: relative; overflow: hidden; padding: 22px 22px 18px 22px; border-radius: 20px;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.18);
  box-shadow: 0 10px 30px rgba(0,0,0,0.35);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease; }
.card:hover{ transform: translateY(-2px); box-shadow: 0 16px 40px rgba(0,0,0,0.45); border-color: rgba(255,255,255,0.28); }
.card .accent{ position: absolute; left: 0; top: 0; bottom: 0; width: 10px; background: linear-gradient(180deg,#818cf8,#22d3ee); }
.icon{ width:84px;height:84px;border-radius:50%; display:grid; place-items:center;
  background: rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.20); font-size:36px; margin-bottom:10px; }
.card h3{ margin:6px 0 4px 0; font-size:1.25rem; color:#fff; }
.card p{ margin:0; color:#CBD5E1; line-height:1.35; }
.actions{ display:flex; gap:12px; align-items:center; margin-top:14px; }
.btn{ padding:10px 18px; border-radius:12px; background:rgba(255,255,255,0.10);
  border:1px solid rgba(255,255,255,0.22); color:#fff; text-decoration:none; font-weight:600;
  transition: background .15s ease, border-color .15s ease, transform .15s ease; }
.btn:hover{ background:rgba(255,255,255,0.16); border-color:rgba(255,255,255,0.32); transform: translateY(-1px); }
.src{ color:#93C5FD; opacity:.9; text-decoration:none; }
.src:hover{ text-decoration:underline; opacity:1; }
h1,h2{ color:#fff; } .subtitle{ color:#CBD5E1; margin-top:-6px; }
</style>
""", unsafe_allow_html=True)

# ---------- DADOS ----------
APPS = [
    {
        "name": "Função Degrau",
        "desc": "Ajuste e visualização de curvas com degraus.",
        "emoji": "📈",
        "url": "https://ajustedefuncaodegrau.streamlit.app",
        "github": "https://github.com/MarioNunes35/Fun-o-degrau/blob/main/degrau.py",
        "accent": "linear-gradient(180deg, #818cf8, #22d3ee)",
    },
    {
        "name": "Ajuste de Eixo e de Tempo",
        "desc": "Corrige deslocamentos de eixo e tempo em séries.",
        "emoji": "🧭",
        "url": "https://ajustedeeixo.streamlit.app",
        "github": "https://github.com/MarioNunes35/Ajuste-de-eixo-e-de-tempo/blob/f7add251a4ed88a0f6be680dc31e8545b6763012/ajustedeeixo.py",
        "accent": "linear-gradient(180deg, #38bdf8, #0ea5e9)",
    },
    {
        "name": "Conversor de Tempo",
        "desc": "Converte formatos mm:ss ↔ s com utilitários práticos.",
        "emoji": "⏱️",
        "url": "https://conversordetempo.streamlit.app",
        "github": "https://github.com/MarioNunes35/conversordetempo/blob/main/conversor-de-tempo.py",
        "accent": "linear-gradient(180deg, #10b981, #22c55e)",
    },
    {
        "name": "Conversor nm → bar",
        "desc": "Converte leituras em nm para bar (calibração).",
        "emoji": "📏",
        "url": "https://conversor-de-nm-para-bar.streamlit.app",
        "github": "https://github.com/MarioNunes35/Conversor-de-nm-para-bar/blob/main/conversor-de-nm-para-bar.py",
        "accent": "linear-gradient(180deg, #f59e0b, #f97316)",
    },
]

# ---------- TOPO + BUSCA ----------
st.markdown('<div class="nav"><span class="brand">MN • Apps</span></div>', unsafe_allow_html=True)
st.markdown("### Seu portal de aplicativos")
st.markdown('<p class="subtitle">Rápido, organizado e bonito — clique e abra em nova aba.</p>', unsafe_allow_html=True)

q = st.text_input("Buscar", placeholder="Buscar aplicativos…", label_visibility="collapsed").strip().lower()
apps = [a for a in APPS if q in a["name"].lower() or q in a["desc"].lower()] if q else APPS

# ---------- HTML DOS CARDS ----------
def card_html(a):
    # cada card é um bloco HTML completo e bem-formado
    return f"""
    <div class="card">
      <div class="accent" style="background:{a['accent']};"></div>
      <div class="icon">{a['emoji']}</div>
      <h3>{a['name']}</h3>
      <p>{a['desc']}</p>
      <div class="actions">
        <a class="btn" href="{a['url']}" target="_blank" rel="noopener">Abrir →</a>
        <a class="src" href="{a['github']}" target="_blank" rel="noopener">Código-fonte</a>
      </div>
    </div>
    """

html = '<div class="grid">' + "".join(card_html(a) for a in apps) + '</div>'
st.markdown(html, unsafe_allow_html=True)  # <— importante: unsafe_allow_html=True


