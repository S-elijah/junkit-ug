# JunkIt - Illegal Dumping Reporting Platform
# Built by a Victoria University Software Engineering Student
# RELX Environmental Challenge 2026

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# App Configuration
st.set_page_config(
    page_title="JunkIt UG",
    page_icon="🗑️",
    layout="wide"
)

# File to store reports
DATA_FILE = "junkit_reports.csv"

# Initialise data file if it doesn't exist,
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["id", "location", "description", "status", "date", "reporter"])
    df.to_csv(DATA_FILE, index=False)

# Helper Functions
def load_reports():
    """Load all reports from CSV file"""
    return pd.read_csv(DATA_FILE)

def save_report(location, description, reporter):
    """Save a new report to CSV"""
    df = load_reports()
    new_id = len(df) + 1
    new_row = {
        "id": new_id,
        "location": location,
        "description": description,
        "status": "Pending",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "reporter": reporter
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    return new_id

def update_status(report_id, new_status):
    """Update the status of a report"""
    df = load_reports()
    if report_id in df["id"].values:
        df.loc[df["id"] == report_id, "status"] = new_status
        df.to_csv(DATA_FILE, index=False)
        return True
    return False

def get_stats():
    """Get summary statistics"""
    df = load_reports()
    if len(df) == 0:
        return 0, 0, 0, 0
    total = len(df)
    pending = len(df[df["status"] == "Pending"])
    acknowledged = len(df[df["status"] == "Acknowledged"])
    resolved = len(df[df["status"] == "Resolved"])
    return total, pending, acknowledged, resolved

# Sidebar Navigation
st.sidebar.title("🗑️ JunkIt UG")
st.sidebar.subheader("Report Waste. Restore Clean.")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["📝 Report Dumping", "📊 View Reports", "📈 Statistics", "ℹ️ About JunkIt"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Built with Python & Streamlit")
st.sidebar.caption("Victoria University Kampala")
st.sidebar.caption("RELX Challenge 2026")

# Report Dumping
if page == "📝 Report Dumping":
    st.title("📝 Report Illegal Dumping")
    st.markdown("Spot it. Snap it. **JunkIt.**")
    st.markdown("---")

    with st.form("report_form"):
        reporter_name = st.text_input("Your Name (optional)", placeholder="Anonymous Reporter")
        location = st.text_input("Location of Dumping *", 
                                  placeholder="e.g., Near Wandegeya Market, behind the taxi park")
        description = st.text_area("Describe What You See *", 
                                    placeholder="e.g., Piles of plastic waste and food scraps dumped in the drainage channel")
        
        st.markdown("*Required fields")
        submitted = st.form_submit_button("🚀 JunkIt! Submit Report")

        if submitted:
            if location and description:
                report_id = save_report(location, description, reporter_name if reporter_name else "Anonymous")
                st.success(f"✅ Report #{report_id} submitted successfully!")
                st.balloons()
                st.info("Your report has been logged. Authorities can now see and act on it.")
            else:
                st.error("❌ Please fill in both location and description.")

    st.markdown("---")
    st.markdown("### Why Report?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🚫 Stop Flooding**")
        st.caption("Blocked drainage causes floods.")
    with col2:
        st.markdown("**🦟 Prevent Disease**")
        st.caption("Dumped waste breeds mosquitos and spreads cholera.")
    with col3:
        st.markdown("**🌍 Protect Uganda**")
        st.caption("Keep our wetlands and communities clean.")

# View Reports
elif page == "📊 View Reports":
    st.title("📊 All Dumping Reports")
    st.markdown("Track what's been reported and their current status.")
    st.markdown("---")

    df = load_reports()

    if len(df) == 0:
        st.info("No reports submitted yet. Be the first to JunkIt!")
    else:
        # Filters
        status_filter = st.selectbox("Filter by Status", ["All", "Pending", "Acknowledged", "Resolved"])
        
        if status_filter != "All":
            df = df[df["status"] == status_filter]
        
        st.markdown(f"**Showing {len(df)} reports**")
        
        # Display reports
        for _, row in df.iterrows():
            with st.expander(f"Report #{int(row['id'])} - {row['location']} ({row['status']})"):
                st.markdown(f"**Location:** {row['location']}")
                st.markdown(f"**Description:** {row['description']}")
                st.markdown(f"**Date:** {row['date']}")
                st.markdown(f"**Reporter:** {row['reporter']}")
                st.markdown(f"**Status:** `{row['status']}`")

    # Admin: Update Status
    st.markdown("---")
    st.markdown("### 🔧 Update Report Status (Admin)")

    with st.form("update_form"):
        report_id = st.number_input("Report ID to update", min_value=1, step=1)
        new_status = st.selectbox("New Status", ["Pending", "Acknowledged", "Resolved"])
        update_submitted = st.form_submit_button("Update Status")

        if update_submitted:
            if update_status(report_id, new_status):
                st.success(f"✅ Report #{report_id} updated to '{new_status}'")
            else:
                st.error("❌ Report ID not found.")

# Statistics 
elif page == "📈 Statistics":
    st.title("📈 JunkIt Statistics")
    st.markdown("See the impact of community reporting.")
    st.markdown("---")

    total, pending, acknowledged, resolved = get_stats()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Reports", total)
    with col2:
        st.metric("Pending", pending, delta_color="off")
    with col3:
        st.metric("Acknowledged", acknowledged)
    with col4:
        st.metric("Resolved ✅", resolved)

    st.markdown("---")
    
    if total > 0:
        # Simple bar chart
        chart_data = pd.DataFrame({
            "Status": ["Pending", "Acknowledged", "Resolved"],
            "Count": [pending, acknowledged, resolved]
        })
        st.bar_chart(chart_data.set_index("Status"))
    else:
        st.info("Submit reports to see statistics here.")
# About JunkIt 
elif page == "ℹ️ About JunkIt":
    st.title("ℹ️ About JunkIt")
    st.markdown("---")
    
    st.markdown("""
    ### What is JunkIt?
    JunkIt is a community-driven platform that empowers Ugandans to report illegal waste dumping, 
    track report progress, and help local authorities identify problem areas for cleaner, 
    healthier neighbourhoods.
    
    # Why JunkIt?
    - 🚫 Illegal dumping blocks drainage and causes flooding
    - 🦟 Dumped waste spreads diseases like cholera and malaria  
    - 🌍 Our wetlands and environment need protection
    - 📱 Everyone should have a voice in keeping their community clean
    
    ### How It Works
    1. Spot illegal dumping in your area
    2. Snap a photo (coming soon) and note the location
    3. JunkIt! Submit your report
    4.Track progress as authorities respond
    
    ### Built For RELX Environmental Challenge 2026
    This prototype was built by a first-year Software Engineering student at 
    Victoria University Kampala, demonstrating how basic Python skills can 
    create tools for real community impact.
    
    ### Future Plans
    - 📸 Photo upload for evidence
    - 📍 GPS auto-location
    - 📱 Mobile app for iOS and Android
    - 📡 USSD access for basic phones
    - 🗺️ Interactive hotspot map
    - 📲 SMS alerts to local authorities
    
  JunkIt — Report Waste. Restore Clean.**
    """)

# Footer 
st.markdown("---")
st.caption("© 2026 JunkIt UG | Built for RELX Environmental Challenge | Victoria University Kampala")
