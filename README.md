# Portal de Apps (Streamlit)

Portal em Streamlit que lista sua suíte de aplicativos com ícones.
Cada cartão abre o aplicativo publicado no Streamlit Cloud e o link do código-fonte no GitHub.

## Como usar
1. Faça upload destes arquivos para um novo repositório GitHub.
2. No Streamlit Community Cloud, crie um app apontando para `streamlit_app.py`.
3. Pronto! Os botões **Abrir** levam para:
   - https://ajustedefuncaodegrau.streamlit.app
   - https://ajustedeeixo.streamlit.app
   - https://conversordetempo.streamlit.app
   - https://conversor-de-nm-para-bar.streamlit.app

## Estrutura
```
.
├─ streamlit_app.py
├─ requirements.txt
├─ runtime.txt
└─ assets/
   ├─ degrau.png
   ├─ eixo_tempo.png
   ├─ tempo.png
   └─ nm_bar.png
```
