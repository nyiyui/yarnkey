#!/usr/bin/env python3
# Calculate error rate per letter
import sys
import json
import csv
from diff_match_patch import diff_match_patch
from collections import defaultdict


# (want, got)
total_errs = defaultdict(lambda: [0, 0])
dmp = diff_match_patch()
for i, line in enumerate(sys.stdin):
    ts, data = line.split(" ", 1)
    data = json.loads(data)
    diffs = dmp.diff_main(data["target"], data["text"])
    # print(data['target'], file=sys.stderr)
    # print(data['text'], file=sys.stderr)
    for j, diff in enumerate(filter(lambda diff: diff[0] == 0, diffs)):
        for c in diff[1]:
            total_errs[c][1] += 1
    diffs = list(filter(lambda diff: diff[0] != 0, diffs))
    errs = []  # (line_index, diff_index, want, got)
    skip_next = False
    for j, diff in enumerate(diffs):
        if skip_next or j == len(diffs) - 1:
            # don't handle last diff as it's covered in a previous loop
            continue
        n = diffs[j + 1]
        if diff[0] != n[0]:
            skip_next = True
            # pair of add and rms
            if diff[0] == 1:
                want = n[1]
                got = diff[1]
            elif diff[0] == -1:
                want = diff[1]
                got = n[1]
            errs.append((i, j, want, got))
            for c in want:
                total_errs[c][0] += 1
                total_errs[c][1] += 1
    # print('\n'.join(map(repr, diffs)))
    # print(errs, file=sys.stderr)
# print(total_errs, file=sys.stderr)

w = csv.writer(sys.stdout)
w.writerow(["letter", "percent", "errors", "total"])
for key in sorted(total_errs.keys()):
    errs, total = total_errs[key]
    w.writerow([json.dumps(key), f"{errs*100/total:0f}", errs, total])
