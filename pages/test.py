import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import streamlit as st

def response_time(df):
    st.title("DataRobot Website Response Time")

    # Convert the 'time' column to datetime format
    df['time'] = pd.to_datetime(df['time'])

    # Create line chart
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['time'], df['response_time'], color='cyan',
            label='Response Time', marker='o', linewidth=2)

    # Customize the plot
    ax.tick_params(axis='y', color='white')
    plt.xlabel("Time", color='white', size=10)
    plt.ylabel("Response Time (ms)", color='white', size=10)
    plt.xticks(rotation=25, color='white', ha='right', size=6)
    plt.yticks(size=6, color='white')
    plt.style.use("dark_background")

    # Set locator and formatter for x-axis ticks
    n = 7  # Number of ticks
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=(24 // n)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    # Set minor locator for more frequent markers
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=(24 // n) * 2))

    # Display the same number of markers as ticks
    ax.xaxis.set_minor_locator(MultipleLocator(base=(24 // n)))

    fig.tight_layout()
    st.pyplot(fig)

# Read in CSV Files
datarobot_response_time = pd.read_csv('./response_time/datarobot.com.csv')

# Call matplotlib line graph
response_time(datarobot_response_time)