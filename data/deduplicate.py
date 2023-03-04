#!/usr/bin/env python3
# Deduplicates duplicate records by session UUID
import sys
import json
from dateutil.parser import parse


records = {}
for i, line in enumerate(sys.stdin):
    if line.strip() == "":
        continue
    ts, data = line.split(" ", 1)
    data = json.loads(data)
    currentUUID = data["currentUUID"]
    if currentUUID in records:
        a_ts = parse(records[currentUUID][0])
        b_ts = parse(ts)
        if b_ts > a_ts:
            records[currentUUID] = (ts, data)
    else:
        records[currentUUID] = (ts, data)
    records[data["currentUUID"]]

for record in records.values():
    ts, data = record
    print(f"{ts} {json.dumps(data)}")
