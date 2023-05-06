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


# Buttons to navigate to different pages
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    if st.button("Dashboard 1"):
        st.experimental_set_query_params(dashboard="dashboard_1")
    if st.button("Dashboard 2"):
        st.experimental_set_query_params(dashboard="dashboard_2")
with col3:
    st.write("")

query_params = st.experimental_get_query_params()

# Navigation logic based on the buttons clicked
if "dashboard" in query_params:
    if query_params["dashboard"][0] == "dashboard_1":
        
        st.write("This is Dashboard 1")
    elif query_params["dashboard"][0] == "dashboard_2":
       
        st.write("This is Dashboard 2")
else:
    st.write("Select a dashboard to view")
