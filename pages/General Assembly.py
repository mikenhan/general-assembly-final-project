import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="General Assembly", page_icon="🤖")

st.markdown("# General Assembly")
st.sidebar.header("General Assembly")
st.write(
    """
    https://generalassemb.ly
    """
)

# Create the response time bar chart using Streamlit
def response_time(df):
    st.title("General Assembly Website Reponse Time")
    st.text("Scroll to zoom in and out")

    df['time'] = pd.to_datetime(df['time'])

    st.bar_chart(df, y='response_time', x='time')

# Create the response time line graph
def http_response(df):
    # set figure and size
    fig, ax = plt.subplots()
    st.title('General Assembly Website Reponse Time')

    # Assign the x and y label
    plt.xlabel("Time", size=8)
    # rotate and align the y label
    plt.ylabel("Response Time (ms)", size=8)

    # create the line graph
    ax.plot(df['time'], df['response_time'],
            color='navy',
            linewidth=1)
    
    # tighten the layout and display
    fig.tight_layout()
    st.pyplot(fig)

# Create average response time function
def average_response(df):
    st.subheader("Average Response Time")
    response_time_ms = int(np.round(df.iloc[:, 1].mean()))
    result = f"{response_time_ms} ms"
    st.write(result)


# Read in CSV Files
ga_response_time = pd.read_csv("./response_time/generalassemb.ly.csv")
ga_response = pd.read_csv('./response/generalassemb.ly.csv')

# Call Average Response time Funtion
average_response(ga_response_time)

# Call the Streamlit bar chart
response_time(ga_response_time)
st.button("Refresh") # add in refresh button

# Call matplotlib line graph
http_response(ga_response_time)
