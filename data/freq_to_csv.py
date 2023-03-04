#!/usr/bin/env python3
# Convert JSON frequency data to a nice csv file
import sys
import json
import csv
from statistics import median


data = json.load(sys.stdin)
monograms = data["monograms"]
bigrams = data["bigrams"]
w = csv.writer(sys.stdout)
w.writerow(
    [
        "ngram",
        "monogram_delta_mean",
        "monogram_delta_median",
        "bigram_delta_mean",
        "bigram_delta_median",
    ]
)
print(monograms, file=sys.stderr)
for monogram, data in monograms.items():
    deltas = list(map(lambda a: a[0], data))
    w.writerow(
        [json.dumps(monogram), sum(deltas) / len(deltas), median(deltas), -1, -1]
    )
for bigram, data in bigrams.items():
    deltas = list(map(lambda a: a[0], data))
    w.writerow(
        [
            json.dumps(bigram),
            -1,
            -1,
            sum(deltas) / len(deltas),
            median(deltas),
        ]
    )
