# Built with pure intention. For the Splendids. For the makers.

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
        st.info("🎨 **Aura (Vision):**")
        st.write("Defining the emotional heart and the 'Big Idea' for the Splendids.")
        
    with row1_col2:
        st.warning("🪨 **Basalt (Skeptic):**")
        st.write("Identifying the 'sticky' points and logistical gaps in the plan.")

    with row2_col1:
        st.header("📚 Coda (The Researcher)")
        st.write("**Protocol Active:**")
        st.write("1. **Triangulate:** Identifying 3 historical low-budget successes.")
        st.write("2. **Library Search:** Connecting to Pedagogy of the Oppressed/Social Prescribing.")
        st.write("3. **The Consult:** Formulating a deep-thinking question for the community.")

    with row2_col2:
        st.success("🛠️ **Drift (The Scrapper):**")
        st.write("Finding the zero-cost, accessible tools to make this excel right now.")

    with row3_col1:
        st.header("📣 **Echo (Community):**")
        st.write("Ensuring this reaches the library kids and those in need of opportunity.")

    with row3_col2:
        st.header("🎯 **Prime (The Lead):**")
        st.write("**Cross-Reading Status:** Evaluating all outputs...")
        st.write("Final 'Perfection Flow' generated based on collective consensus.")
