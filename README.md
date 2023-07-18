# PagePulse 
A website monitoring application that will chart response time and status code response.
### General Assembly Python Programming - Final Project

## How To Use This
1. Install Python3.10 for your operating system
2. Run `pip install -r requirements.txt`
3. Configure the URLs you wish to monitor in data.py
4. Run `app.py` to start data collection and the streamlit app
## Features
- import requests, csv, time, os. from urllib.parse import urlparse
- create list of websites to check
- create check website function
    - try/except.
    - set variables. start time, response, end time
    - if else statement to get 200. print results for each.
    - calculate response time