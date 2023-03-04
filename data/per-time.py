#!/usr/bin/env python3
import sys


times_path = sys.argv[1]
with open(times_path) as f:
    times = set(map(lambda line: line.strip(), f))

for i, line in enumerate(sys.stdin):
    ts, data = line.split(" ", 1)
    # contain match
    # TODO: deduplicate
    skip = False
    # for time in times:
    #    if time in ts:
    #        print(line, end='')
    #        skip = True
    #        continue
    if not skip:
        # strict match
        if ts in times:
            print(line, end="")
            continue
