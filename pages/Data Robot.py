import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="DataRobot", page_icon="🤖")


st.markdown("# DataRobot")
st.sidebar.header("DataRobot")
st.write(
    """
    https://datarobot.com
    """
)

# Create the line plot function
def response_time(df):

    st.title("DataRobot Website Reponse Time")

    # Create bar chart
    fig, ax = plt.subplots(figsize=(6,3))

    # Create line chart
    ax.plot(df.iloc[:, 0], df.iloc[:, 1], color='orange',
            label='Response Time', marker='o', linewidth=2)

    # Customize the plot
    ax.tick_params(axis='y', color='white')
    plt.xlabel("Time", color='white', size=10)
    plt.ylabel("Response Time (ms)", color='white', size=10)
    plt.xticks(rotation=25, color='white', ha='right', size=6)
    plt.yticks(size=6)
    plt.xlim(0, 10)
    plt.style.use("dark_background")

    st.pyplot(fig)

# Create average response time function
def average_response(df):
    st.subheader("Average Response Time")
    response_time_ms = int(np.round(df.iloc[:, 1].mean()))
    st.write(f"{response_time_ms} ms")

# Create overall uptime function
def overall_uptime(df):
    st.subheader("Overall uptime")
    is_200 = len(df[df.iloc[:, 2] == 1])
    length = len(df.iloc[:, 2])
    average = int((is_200 / length) * 100)
    st.write(f"{average} %")

# Read in CSV Files
datarobot_response_time = pd.read_csv('./response_time/datarobot.com.csv')
datarobot_response = pd.read_csv('./response/datarobot.com.csv')

# CAll overall uptime function
overall_uptime(datarobot_response)

# Call Average Response time Funtion
average_response(datarobot_response_time)

# Call matplotlib line graph
response_time(datarobot_response_time)
st.button("Refresh") # add in refresh button