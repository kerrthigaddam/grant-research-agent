import streamlit as st
import pandas as pd
from modules.proposal_writer import generate_proposal
st.title("Claude-Powered Grant Research Agent")
org_name = st.text_input("Organization Name")
mission = st.text_area("Mission Statement")
if st.button("Find Grants"):

    grants = pd.read_csv("data/grants.csv")

    if "education" in mission.lower():
        matches = grants[grants["Category"] == "Education"]

    elif "health" in mission.lower():
        matches = grants[grants["Category"] == "Healthcare"]

    elif "technology" in mission.lower():
        matches = grants[grants["Category"] == "Technology"]

    else:
        matches = grants

    st.success(f"Found {len(matches)} matching grants")

    st.dataframe(matches)

if st.button("Generate Proposal"):

    proposal = generate_proposal(
        org_name,
        mission
    )

    st.subheader("Grant Proposal Draft")

    st.text_area(
        "Generated Proposal",
        proposal,
        height=300
    )