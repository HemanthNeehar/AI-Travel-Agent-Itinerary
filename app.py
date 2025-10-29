from src.core.planner import TravelPlanner
import streamlit as st
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itinerary Planner")
st.write("Plan your day trip itinerary by entering your city and interests")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Enter your city name for your trip")
    interests = st.text_input("Enter your interests (comma separated)")
    submitted = st.form_submit_button("Generate itinerary")

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()

            st.subheader("📄 Your Itineary")
            st.markdown(itinerary)
        else:
            st.markdown("Please fill City and Interests to generate itinerary")