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


def response_time(df):

    st.title("DataRobot Website Reponse Time")

    # Create bar chart
    fig, ax = plt.subplots(figsize=(24,12))

    # Create line chart
    ax.plot(df['time'], df['response_time'], color='orange',
             label='Response Time', marker='o')

    # Customize the plot
    plt.xlabel("Time", color='white')
    plt.ylabel("Response Time (ms)", color='white')
    ax.tick_params(axis='y', color='white')
    plt.xticks(rotation=45, color='white', ha='right')
    plt.xlim(0, 10)
    plt.locator_params(axis='x', nbins=20)
    plt.style.use("dark_background")

    st.pyplot(fig)


datarobot = pd.read_csv('./response_time/datarobot.com.csv')

response_time(datarobot)
