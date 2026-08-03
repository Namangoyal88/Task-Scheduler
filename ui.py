import json
import pandas as pd
import streamlit as st

from planner.planner import GoalPlanner

st.set_page_config(
    page_title="Planner AI",
    page_icon="📝",
    layout="wide"
)

planner = GoalPlanner()

st.title("📝 Planner AI")
st.write("Generate an AI-powered task plan for your goals.")

goal = st.text_input(
    "Goal",
    placeholder="e.g. Learn conversational Spanish"
)

col1, col2 = st.columns(2)

with col1:
    timeframe = st.selectbox(
        "Timeframe",
        ["MONTHLY", "YEARLY"]
    )

with col2:
    granularity = st.selectbox(
        "Granularity",
        ["DAILY", "WEEKLY", "MONTHLY"]
    )

start_date = st.date_input(
    "Start Date"
)

if st.button("Generate Plan", use_container_width=True):

    if not goal.strip():
        st.error("Please enter a goal.")
        st.stop()

    with st.spinner("Generating plan..."):

        result = planner.generate_plan(
            goal=goal,
            timeframe=timeframe,
            granularity=granularity,
            start_date=str(start_date)
        )

    if result["status"] != "success":

        st.warning(result["message"])

    else:

        st.success("Plan generated successfully!")

        df = pd.DataFrame(result["tasks"])

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download JSON",
            data=json.dumps(result["tasks"], indent=4),
            file_name="tasks.json",
            mime="application/json"
        )