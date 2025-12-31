
# # Licensed under the MIT License. See LICENSE file for details.
 with pure intention. For the Splendids. For the makers.

import streamlit as st
import time
import json
from datetime import datetime
import random

# ========== CONFIGURATION ==========
st.set_page_config(page_title="Splendid Swarm Pro", layout="wide", page_icon="🌙")

# Custom CSS for the Night Revolution Vibe
st.markdown("""
<style>
    .stStatus { background: linear-gradient(90deg, #1a1a2e 0%, #16213e 100%); border-radius: 10px; padding: 1rem; border-left: 4px solid #ff6b6b; }
    .actor-card { border-radius: 15px; padding: 1.5rem; margin: 0.5rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); color: white; }
    .aura-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .basalt-card { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
    .coda-card { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    .drift-card { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
    .echo-card { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
    .chatty-card { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); color: #333; }
</style>
""", unsafe_allow_html=True)

# ========== TITLE ==========
st.title("🌙 The Night Revolution PRO")
st.markdown("*Architecture by The Splendids | Built for Proper Research*")

# ========== SIDEBAR SETTINGS ==========
with st.sidebar:
    st.header("⚙️ Swarm DNA")
    engine = st.selectbox("Primary Engine", ["Gemini 1.5 Pro", "Claude 3.5", "Grok-1", "DeepSeek V3"])
    
    st.subheader("Fine-Tune Voices")
    aura_temp = st.slider("🎨 Aura (Vision)", 0.0, 1.0, 0.9)
    basalt_temp = st.slider("🪨 Basalt (Logic)", 0.0, 1.0, 0.2)
    coda_temp = st.slider("📚 Coda (Research)", 0.0, 1.0, 0.3)
    drift_temp = st.slider("🛠️ Drift (Pragmatic)", 0.0, 1.0, 0.7)
    echo_temp = st.slider("📣 Echo (Heart)", 0.0, 1.0, 0.6)
    chatty_temp = st.slider("💬 Chatty Ji (Flow)", 0.0, 1.0, 0.8)

# ========== ACTOR DICTIONARY ==========
ACTORS = {
    "aura": {"name": "🎨 Aura: The Vision", "color": "aura-card", "temp": aura_temp, "role": "Creative possibilities and legendary potential."},
    "basalt": {"name": "🪨 Basalt: The Logic", "color": "basalt-card", "temp": basalt_temp, "role": "Structural gaps, risks, and stress-tests."},
    "coda": {"name": "📚 Coda: The Researcher", "color": "coda-card", "temp": coda_temp, "role": "Historical patterns and data-driven context."},
    "drift": {"name": "🛠️ Drift: The Scrapper", "color": "drift-card", "temp": drift_temp, "role": "Zero-cost tools and street-smart hacks."},
    "echo": {"name": "📣 Echo: The Community", "color": "echo-card", "temp": echo_temp, "role": "Inclusion, empathy, and protecting the vulnerable."},
    "chatty_ji": {"name": "💬 Chatty Ji: The Polish", "color": "chatty-card", "temp": chatty_temp, "role": "Conversational warmth and clarity."}
}

# ========== SIMULATION ENGINE ==========
def get_perspective(actor, query):
    # These are placeholders that act as 'DNA Templates'
    responses = {
        "aura": f"I see a magnificent future for {query}. We should treat this as a ritual of growth.",
        "basalt": f"We must identify the single point of failure in {query} before moving forward.",
        "coda": f"Historically, {query} follows the pattern of decentralized community movements.",
        "drift": f"We can build {query} using open-source tools and recycled local knowledge.",
        "echo": f"The heart of {query} must be accessible to the library kids and the elderly alike.",
        "chatty_ji": f"Let's make {query} feel like a warm invitation rather than a difficult task."
    }
    return responses.get(actor, "Processing...")

# ========== MAIN INPUT ==========
query = st.text_area("🌌 What is our mission tonight?", placeholder="Enter your goal...", height=100)

if st.button("🚀 ACTIVATE SWARM", type="primary", use_container_width=True):
    if query:
        # Phase 1: Awakening
        with st.status("🤝 The Splendid Swarm is deliberating...", expanded=True) as status:
            for actor_key in ACTORS:
                st.write(f"{ACTORS[actor_key]['name']} is analyzing...")
                time.sleep(0.3)
            status.update(label="✅ Swarm Synchronized!", state="complete", expanded=False)

        # Phase 2: Display Cards
        st.subheader("🎭 The Council Perspectives")
        full_report = f"MISSION: {query}\nDATE: {datetime.now()}\nENGINE: {engine}\n"
        full_report += "="*40 + "\n\n"
        
        cols = st.columns(2)
        for idx, (key, data) in enumerate(ACTORS.items()):
            with cols[idx % 2]:
                st.markdown(f"<div class='actor-card {data['color']}'><h3>{data['name']}</h3></div>", unsafe_allow_html=True)
                ans = get_perspective(key, query)
                st.write(ans)
                full_report += f"[{data['name'].upper()}]\n{ans}\n\n"

        # Phase 3: The Paper
        st.divider()
        st.subheader("📜 The Unified Splendid Paper")
        st.caption("Copy this for Claude, Grok, or DeepSeek to perform the final cross-read.")
        st.text_area("Master Output:", full_report, height=300)
        st.download_button("📥 Download Consensus", full_report, file_name="swarm_consensus.txt")
    else:
        st.warning("Please enter a mission first.")
