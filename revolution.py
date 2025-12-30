# Built with pure intention. For the Splendids. For the makers.

import streamlit as st

st.set_page_config(page_title="Splendid Swarm", layout="wide")
st.title("🌙 The Night Revolution")
st.markdown("*Research, Consult, and Excel.*")

query = st.text_area("What is our mission tonight?", placeholder="Enter one goal here...")

if st.button("Activate Swarm"):
    full_report = f"MISSION ENQUIRY: {query}\n\n"
    
    # Grid for the 6 Actors
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    c5, c6 = st.columns(2)

    with c1:
        st.info("🎨 Aura: The Vision")
        full_report += "AURA: Defining the creative spark...\n"
    with c2:
        st.warning("🪨 Basalt: The Logic")
        full_report += "BASALT: Testing for structural gaps...\n"
    with c3:
        st.header("📚 Coda: Research")
        full_report += "CODA: Triangulating historical success...\n"
    with c4:
        st.success("🛠️ Drift: Scrapper")
        full_report += "DRIFT: Finding zero-cost tools...\n"
    with c5:
        st.header("📣 Echo: Community")
        full_report += "ECHO: Protecting the library kids...\n"
    with c6:
        st.header("💬 Chatty Ji: Polish")
        full_report += "CHATTY JI: Smoothing the conversational flow...\n"

    st.divider()
    st.subheader("📋 The Unified Splendid Paper")
    st.text_area("Master Output (Copy this for Claude/Grok/DeepSeek):", full_report, height=300)
    st.download_button("Download Consensus Paper", full_report)
