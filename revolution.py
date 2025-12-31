# Built with pure intention. For the Splendids. For the makers.

import streamlit as st

# Setup the "Sticky-Screen" UI
st.set_page_config(page_title="Splendid Swarm", layout="wide")
st.title("🌙 The Night Revolution")
st.markdown("*Research, Consult, and Excel.*")

# The Single Input
query = st.text_area("What is our mission tonight?", placeholder="Enter one goal here...")

if st.button("Activate Swarm"):
    # 1. THE STATUS BAR (Visual confirmation the Swarm is waking up)
    with st.status("🤝 The Splendid Swarm is deliberating...", expanded=True) as status:
        st.write("🎨 Aura is dreaming...")
        st.write("📚 Coda is searching the archives...")
        st.write("🪨 Basalt is checking the foundations...")
        st.write("💬 Chatty Ji is polishing the intent...")
        status.update(label="✅ Swarm Synchronized!", state="complete", expanded=False)

    # 2. THE CHORUS DNA (The instructions for the other AIs)
    # This block builds the 'Paper' with specific roles included
    full_report = f"MISSION ENQUIRY: {query}\n"
    full_report += "="*30 + "\n"
    full_report += "INSTRUCTIONS FOR THE CROSS-READ:\n"
    full_report += "- Aura: Bold, innovative potential.\n"
    full_report += "- Basalt: Logical gaps and risks.\n"
    full_report += "- Coda: Historical context and patterns.\n"
    full_report += "- Drift: Zero-cost hacks and tools.\n"
    full_report += "- Echo: Community impact and accessibility.\n"
    full_report += "- Chatty Ji: Warmth and clarity.\n"
    full_report += "="*30 + "\n\n"
    
    # 3. THE UI GRID (Display for your tablet)
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    c5, c6 = st.columns(2)

    with c1:
        st.info("🎨 Aura: The Vision")
        full_report += "AURA [VISION]: Analyzing the creative heart...\n"
    with c2:
        st.warning("🪨 Basalt: The Logic")
        full_report += "BASALT [LOGIC]: Finding structural gaps...\n"
    with c3:
        st.header("📚 Coda: Research")
        full_report += "CODA [RESEARCH]: Triangulating historical success...\n"
    with c4:
        st.success("🛠️ Drift: Scrapper")
        full_report += "DRIFT [SCRAPPY]: Locating zero-cost tools...\n"
    with c5:
        st.header("📣 Echo: Community")
        full_report += "ECHO [HEART]: Ensuring the library kids are protected...\n"
    with c6:
        st.header("💬 Chatty Ji: Polish")
        full_report += "CHATTY JI [FLOW]: Smoothing the conversational path...\n"

    # 4. THE UNIFIED PAPER (For your one-click copy)
    st.divider()
    st.subheader("📋 The Unified Splendid Paper")
    st.markdown("Populate this text into Claude, Grok, or DeepSeek for the final cross-read.")
    st.text_area("Master Output:", full_report, height=400)
    st.download_button("Download Consensus Paper", full_report)
