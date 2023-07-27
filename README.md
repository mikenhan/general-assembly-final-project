# PagePulse 📈
A website monitoring application that will chart response time and status code response.
### General Assembly Python Programming - Final Project


## How To Use This
1. Install Python3.10 for your operating system
2. Run `pip install -r requirements.txt`
3. Configure the URLs you wish to monitor in data.py


## Starting the Application
* If on a Linux or Mac system:
    * run `streamlit run app.py`
    * Run `nohup streamlit run app.py > streamlit.log 2>&1 &` if you wish to free up your terminal
* If on a Windows system:
    * `start streamlit run app.py`
    * `start "" streamlit run app.py` if you wish to free up your Powershell Terminal

## Explaination of the files
- app.py will start data collection and the Streamlit app
- data.py is the data collection script
- Home.py contains the Streamlit Application Data
- Files within the pages directory correspond to individual pages in which you are collecting data.
  - You should modify the names of these files to match the URLs that you are logging


## Problem Statements
- Your problem statement. What is the problem you're trying to solve?
  - Create a customizable Website monitoring tool. Often times companies will look to have something made in house
- A brief summary of your solution to the problem. Make this readable so a person without a technical background could understand how you solve the problem! If you can, include why your solution matters. (Brief: somewhere around 4-6 sentences, but this isn't a hard rule.)
  - I have created a few charts as a demonstration on how response time can be visualized. There are also a few summaries on overall uptime (as a percentage), as well as the average response time (in ms). 
- A summary of your technical solution. This can include more technical descriptions of the work you did.
  - I first started collecting my own data as the free APIs did not provide the information I was looking for. I was able to leverage Streamlit to create multiple pages (each website having it's own). Using what we learned on Pandas and Matplotlib, I was able to generate a line graph (with custom configuation). I then created a bar chart that was interactive using Streamlit. 
- A brief summary of each of the files in your repository.
  - app.py - This will run the data collection script as well as start streamlit
  - Home.py - This is the entrypoint (first page) the app will show a user
  - Data Robot.py - This generates the data robot page
  - General Assembly.py - This geneartes the GA page
  - requirements.txt - list of pip requirements to run this app
- Contact information so people can reach out to you to learn more.
  - Mike Nhan mike.nhan@gmail.com
