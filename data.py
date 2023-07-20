'''
General Assembly - Python Programming
Instructor: Matt Brems
Student: Mike Nhan
Final Project
July 25, 2023
'''
import requests
import csv
import time
import os
from urllib.parse import urlparse

# --------------- Set Variables ---------------
# MODIFY THIS ONLY
websites = ['https://generalassemb.ly',
            'https://datarobot.com']


#####################
#
# DO NOT MODIFY BELOW
#
#####################
response_time_folder = "response_time"
response_folder = "response"

# Check if folder structure has been configured
if not os.path.isdir(response_folder):
    os.mkdir(response_folder)

if not os.path.isdir(response_time_folder):
    os.mkdir(response_time_folder)

# --------------- Function to gather data ---------------


def check_website_status(url):
    try:
        response = requests.get(url)  # gather the response from URL
        response_time = response.elapsed.total_seconds() * 1000

        if response.status_code == 200:
            print(f"{url} is up and running!")  # prints to the terminal
        else:
            print(f"{url} is down! Status {response.status_code}")

        # Save data to it's own individual CSV file
        domain_name = urlparse(url).netloc
        csv_file_1 = f"{response_time_folder}/{domain_name}.csv"
        # had to use not. otherwise new file does not add headers
        response_time_file = not os.path.isfile(csv_file_1)
        # always open in append mode
        with open(csv_file_1, "a", newline='') as file1:
            writer = csv.writer(file1)
            if response_time_file:  # If file does not exist we will create it with the header row
                writer.writerow(['time', 'response_time'])
            # write data to each row
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"),
                            response_time])

        csv_file_2 = f"{response_folder}/{domain_name}.csv"
        response_file = not os.path.isfile(csv_file_2)

        with open(csv_file_2, 'a', newline='') as file2:
            writer = csv.writer(file2)
            if response_file:
                writer.writerow(['time', 'response', 'overall'])

            overall = 1 if response.status_code == 200 else 0
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"),
                            response.status_code, overall])

    except requests.exceptions.RequestException:
        print(f"{url} is down.")  # print this in case of unreachable URL


while True:
    for website in websites:  # iterate through list
        check_website_status(website)  # call the function
    print("------")
    time.sleep(300)  # Checks once a minute.
