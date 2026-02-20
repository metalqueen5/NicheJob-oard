streamlit
python-jobspy
pandas
import streamlit as st
import pandas as pd
from jobspy import scrape_jobs

# --- CONFIGURATION ---
NICHE = "Remote Marketing"  # Change this to your niche!
STRIPE_FEATURED_URL = "https://buy.stripe.com/your_link" # Put your Stripe link here

st.set_page_config(page_title="Niche Jobs", layout="wide")

# --- 1. AUTOMATED SCRAPER FUNCTION ---
def get_fresh_jobs():
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin"],
        search_term=NICHE,
        location="USA",
        results_wanted=10,
        hours_old=72 
    )
    return jobs

# --- 2. THE FRONTEND ---
st.title(f"🚀 {NICHE} Job Board")
st.write("Automatically updated every day.")

# FEATURE 3: ADVERTISING (Simple banner)
st.sidebar.info("📢 Sponsored: [Learn Python on your Phone!](https://affiliate-link.com)")

# FEATURE 2: IN-APP PURCHASES
st.sidebar.header("Employers")
if st.sidebar.button("🌟 Post Featured Job ($49)"):
    st.sidebar.markdown(f"[Click to Pay via Stripe]({STRIPE_FEATURED_URL})")

# --- 3. DISPLAYING THE JOBS ---
try:
    data = get_fresh_jobs()
    for index, row in data.iterrows():
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{row['title']}**")
                st.caption(f"{row['company']} | {row['location']}")
            with col2:
                st.link_button("Apply", row['job_url'])
            st.divider()
except Exception as e:
    st.error("Robot is resting. Refresh in a minute!")
