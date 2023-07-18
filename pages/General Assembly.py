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

    general_assembly['time'] = pd.to_datetime(general_assembly['time'])

    st.bar_chart(df, y='response_time', x='time')

# Create the


def http_response(df):
    # set figure and size
    fig, ax = plt.subplots()
    st.title('General Assembly Website Reponse Time')

    # Assign the x and y label
    plt.xlabel("Time", size=8)
    # rotate and align the y label
    plt.ylabel("Response Time (ms)", size=8)

    # start with a line graph of closing price
    ax.plot(df['time'], df['response_time'],
            color='navy',
            linewidth=1)

    fig.tight_layout()
    st.pyplot(fig)


general_assembly = pd.read_csv("./response_time/generalassemb.ly.csv")

response_time(general_assembly)

st.button("Refresh")

http_response(general_assembly)


# # Create a DataFrame from the data
# df = pd.DataFrame(general_assembly)

# # Display the response time data in a table (optional)
# st.dataframe(df)

# # Dropdown widget to select time frames
# time_frames = [5, 10, 30, 60]
# selected_time_frame = st.selectbox('Select Time Frame (minutes)', time_frames)

# # Create the bar chart using matplotlib
# fig, ax = plt.subplots()
# bars = ax.bar(df['time'], df['response_time'], color='skyblue')

# Add labels to the bars
# for bar in bars:
#     height = bar.get_height()
#     ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
#                 xytext=(0, 3),  # 3 points vertical offset
#                 textcoords="offset points",
#                 ha='center', va='bottom')

# plt.xlabel("Time")
# plt.ylabel("Response Time (ms)")
# plt.title("Website Response Time")
# plt.xticks(rotation=45, ha='right')

# # Show the bar chart using st.pyplot()
# st.pyplot(fig)

# st.button("Refresh")
