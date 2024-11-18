import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Constants
LOGO_PATH = "Campaign-Report_Logo.png"
USERNAME = "ClientX"
PASSWORD = "stratbomb"

# Authentication function
def authenticate(username, password):
    return username == USERNAME and password == PASSWORD

# Function to load CSV
def load_csv(data_source, uploaded_file=None, drive_path=None):
    try:
        if data_source == "Local file upload" and uploaded_file is not None:
            return pd.read_csv(uploaded_file)
        elif data_source == "Google Drive path" and drive_path:
            if os.path.exists(drive_path):
                return pd.read_csv(drive_path)
            else:
                st.error("The specified path does not exist.")
        else:
            st.error("No valid data source selected.")
    except Exception as e:
        st.error(f"Error loading file: {e}")
    return None

# Voter Engagement Report logic
def voter_engagement_report(df):
    # Your voter engagement logic here (refactor as needed)
    # ...

    st.success("Voter Engagement Report Generated.")  # Placeholder

# Election Runup Analysis Report logic
def election_runup_report(df):
    # Your election runup analysis logic here (refactor as needed)
    # ...

    st.success("Election Runup Analysis Report Generated.")  # Placeholder

# Main application
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Login screen
    if not st.session_state.logged_in:
        st.image(LOGO_PATH, width=250)
        st.title("Login to Reporter App")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
    else:
        st.image(LOGO_PATH, width=225)
        st.title("Election Reporter Tool")
        st.divider()

        # Report type selection
        report_type = st.selectbox("What kind of Report do you want to create?",
                                   ["Voter Engagement", "Election Runup Analysis"])

        # Data source selection
        data_source = st.radio("Choose the source of your CSV file:", ["Local file upload", "Google Drive path"])
        uploaded_file = None
        drive_path = None

        if data_source == "Local file upload":
            uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        elif data_source == "Google Drive path":
            drive_path = st.text_input("Enter the path to your CSV file:")

        df = load_csv(data_source, uploaded_file, drive_path)

        if df is not None:
            if report_type == "Voter Engagement":
                voter_engagement_report(df)
            elif report_type == "Election Runup Analysis":
                election_runup_report(df)
        else:
            st.info("Please upload or specify a valid CSV file.")

if __name__ == "__main__":
    main()
