import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------- Set Page Configuration  ---------------
st.set_page_config(page_title="DataRobot", page_icon="🤖")

# --------------- Configure Sidebar Text ---------------
st.sidebar.header("DataRobot")
st.sidebar.write("At DataRobot, we move fast and reward hard work. We expect results but most of all, we love doing work we’re passionate about. We believe that AI will enhance every aspect of business transactions and human interactions to improve how we live, work, play and stay safe. Our vision? For all organizations to adopt Value-Driven AI as a core competency to improve how they run, grow, and optimize their business.")

# --------------- Configure Main Page Text  ---------------
st.markdown("# DataRobot")
st.write(
    """
    https://datarobot.com
    """
)

# --------------- Function for Line Graph ---------------
def response_time(df):
    st.title("DataRobot Website Reponse Time")

    # Set market to go back
    # This can be adjusted as you wish
    markers = 50

    # Create line chart
    fig, ax = plt.subplots(figsize=(16,8))
    # We only want data for the last few rows as specified by markers
    ax.plot(df.iloc[:, 0].tail(markers), df.iloc[:, 1].tail(markers), color='orange',
            label='Response Time', marker='o', linewidth=2)

    # Customize the plot
    ax.tick_params(axis='y', color='white')
    plt.xlabel("Time", color='white', size=30)
    plt.ylabel("Response Time (ms)", color='white', size=25)
    plt.xticks(rotation=25, color='white', ha='right', size=15)
    plt.yticks(size=18, color='white')
    plt.xlim(0, 10)
    plt.ylim(0, max(df.iloc[:, 1].tail(markers)))
    plt.style.use("dark_background")

    fig.tight_layout()
    st.pyplot(fig)

# --------------- Function for Average Response Time ---------------
def average_response(df):
    st.subheader("Average Response Time")
    response_time_ms = int(np.round(df.iloc[:, 1].mean()))
    st.write(f"{response_time_ms} ms")

# --------------- Function for Overall Uptime ---------------
def overall_uptime(df):
    st.subheader("Overall uptime")
    is_200 = len(df[df.iloc[:, 2] == 1])
    length = len(df.iloc[:, 2])
    average = int((is_200 / length) * 100)
    st.write(f"{average} %")

# --------------- Read in CSV Files ---------------
datarobot_response_time = pd.read_csv('./response_time/datarobot.com.csv')
datarobot_response = pd.read_csv('./response/datarobot.com.csv')

# --------------- Reload all Graphs ---------------
st.button("Reload All") 

# --------------- Call Function for Uptime ---------------
overall_uptime(datarobot_response)
# --------------- Call Function for Average Response Time ---------------
average_response(datarobot_response_time)
# --------------- Call Function for Response Time Graph ---------------
response_time(datarobot_response_time)
