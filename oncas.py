# -*- coding: utf-8 -*-
import os
import base64
import streamlit as st

# ===== CONFIGURAÇÃO GERAL =====
st.set_page_config(
    page_title="Prestação de Contas – As Onças Não Rugem à Toa 🐆",
    page_icon="🐆",
    layout="wide"
)

# ===== ESTILOS =====
st.markdown("""
<style>
.block-container { max-width: 1200px; }
body, .block-container {
  background: #fffaf2 !important;
  font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  font-size: 14px; color: #333;
}
h1 {
  font-size: 28px; font-weight: 800; color: #e67e22;
  text-align: center; margin-bottom: 0;
}
h2, h3 { color: #d17b0f; font-weight: 700; }
.hr-thin { border: none; border-top: 2px solid #f4a261; width: 50%; margin: 10px auto; }

/* FOTOS */
.gallery, .nf-wrap {
  display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-top: 10px;
}
.card-photo, .card-nf {
  background: none;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,.15);
  padding: 0;
  transition: transform .2s ease-in-out;
}
.card-photo:hover, .card-nf:hover { transform: scale(1.02); }
.card-photo img { width: 200px; height: auto; border-radius: 10px; }
.card-nf img { width: 430px; height: auto; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# ===== FUNÇÕES =====
BASE_DIR = os.path.join("imagens")

def cabecalho():
    st.markdown("""
    <h1>🐆 Prestação de Contas – As Onças Não Rugem à Toa 💛</h1>
    <div style="text-align:center;font-weight:500;">Gincana Solidária SIPAT 2025 – CETURB/ES</div>
    <hr class="hr-thin">
    """, unsafe_allow_html=True)

def listar_imgs(subpasta):
    pasta = os.path.join(BASE_DIR, subpasta)
    if not os.path.isdir(pasta):
        return []
    return sorted([
        os.path.join(pasta, f) for f in os.listdir(pasta)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

def bloco_fotos(titulo, subpasta, tipo="foto"):
    st.markdown(f"<h3>📸 {titulo}</h3>", unsafe_allow_html=True)
    arquivos = listar_imgs(subpasta)
    if not arquivos:
        st.info("Nenhuma imagem encontrada nesta seção.")
        return
    st.markdown('<div class="gallery">', unsafe_allow_html=True)
    for arq in arquivos:
        with open(arq, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        classe = "card-nf" if tipo == "nf" else "card-photo"
        st.markdown(f'<div class="{classe}"><img src="data:image/jpeg;base64,{b64}" alt=""></div>',
                    unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== ABAS =====
aba1, aba2, aba3 = st.tabs(["📖 Introdução", "🖼️ Fotos", "🧾 Notas Fiscais"])

# ===== ABA 1 =====
with aba1:
    cabecalho()

    # LOGO CENTRALIZADO
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; margin-bottom: 20px;">
            <img src="https://raw.githubusercontent.com/millenasimoncelo/prestacao-oncas/main/imagens/Logo%20onças.png" width="220">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <p style="text-align:justify;">
    A equipe <strong>As Onças Não Rugem à Toa</strong> participou com garra, alegria e muita solidariedade
    da Gincana Solidária da SIPAT 2025. Nosso rugido foi de amor, união e compromisso com o bem — e cada
    doação, cada brinquedo e cada sorriso fez parte dessa história! 💛
    </p>
    <p style="text-align:justify;">
    Aqui está nossa <strong>Prestação de Contas</strong>, feita com transparência, carinho e o mesmo
    entusiasmo que marcou toda a campanha.
    </p>
    """, unsafe_allow_html=True)

# ===== ABA 2 =====
with aba2:
    cabecalho()
    bloco_fotos("Campanha de arrecadação de doações", "1.Campanha")
    bloco_fotos("Compra dos brinquedos", "2.Compra dos brinquedos")
    bloco_fotos("Troca dos brinquedos por estrelinhas", "3.Troca dos brinquedos por estrelinhas")
    bloco_fotos("Resultado da gincana", "4.Resultado da gincana")
    bloco_fotos("Organização e separação", "5.Organização dos brinquedos para entrega")
    bloco_fotos("Entrega às Instituições", "6.Entrega dos brinquedos para a Obra Social")

# ===== ABA 3 =====
with aba3:
    cabecalho()
    bloco_fotos("Notas Fiscais", "7.Notas fiscais", tipo="nf")






