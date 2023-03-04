#!/usr/bin/env python3
# csv-ify error rate and speed for all trials given
import sys
import json
import csv
from collections import defaultdict


w = csv.writer(sys.stdout)
w.writerow(["session_name", "session_uuid", "error rate", "speed"])
for i, line in enumerate(sys.stdin):
    ts, data = line.split(" ", 1)
    data = json.loads(data)
    errRate = data["errCount"] / len(data["target"])
    speed = len(data["text"]) / data["duration"]
    w.writerow([data["sessionName"], data["currentUUID"], errRate, speed])
