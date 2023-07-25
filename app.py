import subprocess
import time

# Popen allows you to run commands and capture the output
data = subprocess.Popen(["python3", "data.py"])

time.sleep(60)

# You can also use it to run multiple commands before waiting
# on a previous one to complete
stream = subprocess.Popen(["streamlit", "run", "Home.py"])
