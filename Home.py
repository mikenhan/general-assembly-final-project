import streamlit as st

# --------------- Set Page Configuration  ---------------
st.set_page_config(
    page_title="PagePulse",
    page_icon="📈",
)

# --------------- Configure Sidebar Text ---------------
st.sidebar.success("Select a site above.")

st.write("# Welcome to PagePulse! 👋")

# --------------- Configure Main Page Text ---------------
st.markdown(
    """
    PagePulse is a website monitoring and response time website
    built with Python and Streamlit for the General Assembly
    Python Programming course.  

    **👈 Select a URL from the sidebar** to see statistics!
    ### Want to learn more?
    - Check out the [repo](https://github.com/mikenhan/general-assembly-final-project) for more information.
    ### Documentation used
    - [Streamlit](https://docs.streamlit.io)
    - [Pandas](https://pandas.pydata.org/docs/)
    - [Numpy](https://numpy.org/doc/)
"""
)
