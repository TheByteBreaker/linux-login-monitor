import time

LOG_FILE = "/var/log/auth.log"  

def follow(file):
    file.seek(0, 2)  
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

with open(LOG_FILE, "r") as logfile:
    loglines = follow(logfile)
    for line in loglines:
        if "session opened for user" in line or "Accepted password" in line:
            print("[LOGIN SUCCESS] " + line.strip())
        elif "Failed password" in line:
            print("[LOGIN FAILED] " + line.strip())
