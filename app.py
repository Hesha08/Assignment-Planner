import streamlit as st
from planner import generate_plan

st.set_page_config(page_title="Assignment Study Planner", layout="centered")

st.title("📚 AI Daily Study Planner")
st.write("Enter today's assignments and get an optimized schedule!")

# User Inputs
available_time = st.number_input("Available study time today (in hours)", min_value=1, max_value=24)

assignments = st.text_area(
    "Enter assignments like this:\n"
    "(Assignment: Math worksheet, priority:3)\n"
    "(Assignment: English essay, priority:5)"
)

if st.button("Generate Plan 🚀"):

    if assignments.strip() == "":
        st.warning("Please enter assignments.")
    else:
        input_text = f"""
        Total available time = {available_time} hours.
        Assignments:
        {assignments}
        """

        with st.spinner("Generating your optimized plan..."):
            result = generate_plan(input_text)

        st.subheader("📅 Your Study Plan")
        st.markdown(result, unsafe_allow_html=True)