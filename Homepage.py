import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
)

st.markdown(
    "<h1 style='text-align: center;'>Predictive Urban Growth and Planning in African Cities</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center;'>Omdena - Nairobi, Kenya Chapter</h3>",
    unsafe_allow_html=True,
)

st.sidebar.success("Select a dashboard above.")

# URLs of the raw .py files on GitHub
dashboard_1_url = "https://raw.githubusercontent.com/Riley-livingston/temporary_streamlit_1/main/pages/1_%F0%9F%93%88_UN%20Accuracy%20Estimate.py"
dashboard_2_url = "https://raw.githubusercontent.com/your_username/your_repository/main/pages/dashboard_2.py"

# Buttons to navigate to different pages
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    if st.button("Dashboard 1"):
        st.session_state.dashboard = "dashboard_1"
    if st.button("Dashboard 2"):
        st.session_state.dashboard = "dashboard_2"
with col3:
    st.write("")

# Navigation logic based on the buttons clicked
if "dashboard" in st.session_state:
    if st.session_state.dashboard == "dashboard_1":
        response = requests.get(dashboard_1_url)
        if response.status_code == 200:
            exec(response.text)
        else:
            st.write("Error loading Dashboard 1. Please check the URL.")
    elif st.session_state.dashboard == "dashboard_2":
        response = requests.get(dashboard_2_url)
        if response.status_code == 200:
            exec(response.text)
        else:
            st.write("Error loading Dashboard 2. Please check the URL.")
else:
    st.write("Select a dashboard to view")
