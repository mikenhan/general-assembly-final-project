import subprocess
import time

data = subprocess.Popen(["python3", "data.py"])

time.sleep(60)

stream = subprocess.Popen(["streamlit", "run", "Home.py"])
