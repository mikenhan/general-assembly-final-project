import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------- Set Page Configuration  ---------------
st.set_page_config(page_title="General Assembly", page_icon="🤖")

# --------------- Configure Sidebar Text ---------------
st.sidebar.header("General Assembly")
st.sidebar.write("Since 2011, General Assembly has transformed tens of thousands of careers through pioneering, experiential education in today’s most in-demand skills. When you learn web development, data, design, business, and more with GA, you get:")
st.sidebar.write("Award-winning curriculum and expert instructors, on campus and online.")
st.sidebar.write("A global, professional community of 40,000-plus full- and part-time alumni.")
st.sidebar.write("Career results from leading-edge courses, with mentorship each step of the way.")

# --------------- Configure Main Page Text  ---------------
st.markdown("# General Assembly")
st.write(
    """
    https://generalassemb.ly
    """
)

# --------------- Function for Streamlit Bar Graph ---------------
def response_time(df):
    st.title("General Assembly Website Reponse Time")
    st.text("Scroll to zoom in and out")

    df['time'] = pd.to_datetime(df['time'])

    st.bar_chart(df, y='response_time', x='time')

# --------------- Function for Response Time Line Graph ---------------
def http_response(df):
    # set figure and size
    fig, ax = plt.subplots()
    st.title('General Assembly Website Reponse Time')

    # Assign the x and y label
    plt.xlabel("Time", size=8)
    plt.ylabel("Response Time (ms)", size=8)

    # Rotate the X tick
    plt.xticks(rotation=25)

    # create the line graph
    ax.plot(df.iloc[:, 0].tail(100), df.iloc[:, 1].tail(100),
            color='cyan',
            linewidth=1)
    
    # tighten the layout and display
    fig.tight_layout()
    st.pyplot(fig)

# --------------- Function for Line Graph ---------------
def average_response(df):
    st.subheader("Average Response Time")
    response_time_ms = int(np.round(df.iloc[:, 1].mean()))
    result = f"{response_time_ms} ms"
    st.write(result)

# --------------- Read in CSV Files ---------------
ga_response_time = pd.read_csv("./response_time/generalassemb.ly.csv")
ga_response = pd.read_csv('./response/generalassemb.ly.csv')


# --------------- Reload all Graphs ---------------
st.button("Reload All") 
# --------------- Call Function for Average Response Time ---------------
average_response(ga_response_time)
# --------------- Call Function for Streamlit Bar Graph ---------------
response_time(ga_response_time)
# --------------- Call Function for Response Time Line Graph ---------------
http_response(ga_response_time)
