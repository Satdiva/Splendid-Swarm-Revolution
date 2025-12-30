import streamlit as st

# Setup the "Sticky-Screen" UI
st.set_page_config(page_title="Splendid Swarm", layout="wide")
st.title("🌙 The Night Revolution")
st.markdown("*Research, Consult, and Excel.*")

# The Single Input
query = st.text_area("What is our mission tonight?", placeholder="Enter one goal here...")

if st.button("Activate Swarm"):
    # We create 3 rows of 2 columns for easy reading on a tablet
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    row3_col1, row3_col2 = st.columns(2)

    with row1_col1:
        st.info("🎨 **Aura (Vision):** Analyzing the creative spark...")
        # AI logic for Aura goes here
        
    with row1_col2:
        st.warning("🪨 **Basalt (Skeptic):** Checking for risks...")
        # AI logic for Basalt goes here

    # ... and so on for the others ...

    st.success("🎯 **Prime (Consensus):** Here is the final 'Perfection Flow' for the Splendids.")
