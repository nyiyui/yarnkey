#!/bin/env python3

from data import Session
from collections import defaultdict
from string import ascii_lowercase
from diff_match_patch import diff_match_patch

dmp = diff_match_patch()


CHARS = ascii_lowercase

def process(sess: Session) -> dict:
    d = dmp.diff_main(sess.data['target'], sess.data['text'])
    missed = defaultdict(int)
    for op, s in d:
        if op == -1:
            for c in s:
                missed[s] += 1
    return sess.data['currentUUID'], missed

if __name__ == '__main__':
    from sys import stdin, stdout, stderr
    from data import parse_line
    import csv

    gtgt = {key: 0 for key in CHARS}
    w = csv.writer(stdout)
    w.writerow(['attemptID'] + sorted(gtgt.keys()))
    w.writerow(['target'] + [gtgt[key] for key in sorted(gtgt.keys())])
    for i, data in enumerate(map(process, map(parse_line, stdin))):
        attemptID, tgt = data
        w.writerow([attemptID] + [tgt[key] for key in sorted(gtgt.keys())])
