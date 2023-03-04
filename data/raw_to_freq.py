#!/usr/bin/env python3
# Convert raw data to frequency data of mono/bigrams in JSON format for easier processing for freq_to_csv.py
import sys
import json
from collections import defaultdict


monograms = defaultdict(list)
bigrams = defaultdict(list)

for i, line in enumerate(sys.stdin):
    ts, data = line.split(" ", 1)
    data = json.loads(data)
    prev_ts = data["start"]
    letters = []
    deltas = []
    for stroke in data["strokes"]:
        received, add, rm = stroke["received"], stroke["add"], stroke["rm"]
        delta = received - prev_ts
        if add != "":
            monogram = add
            if len(letters):
                bigram = letters[-1] + monogram
                delta2 = deltas[-1] + delta
                # print(delta, json.dumps(bigram))
                bigrams[bigram].append((delta2, i))
            monograms[monogram].append((delta, i))
            deltas.append(delta)
            letters.append(add)
        prev_ts = received
    print(
        f"i: {i}\t{len(bigrams)} bigrams\t{len(monograms)} monograms", file=sys.stderr
    )

json.dump(
    dict(
        bigrams=bigrams,
        monograms=monograms,
    ),
    sys.stdout,
)
