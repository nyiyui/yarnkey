#!/usr/bin/env python3

from data import Session
from collections import defaultdict


def timing(sess: Session) -> dict:
    keys = defaultdict(list)
    prev = {"received": sess.data["firstChange"]}
    for stroke in sess.data["strokes"]:
        received, add = stroke["received"], stroke["add"]
        prev_received = prev["received"]
        dt = received - prev_received
        keys[add].append(dt)
        prev = stroke
    return dict(keys)


def count(sess: Session) -> tuple:
    tgt = defaultdict(int)
    for key in sess.data["target"]:
        tgt[key] += 1
    act = defaultdict(int)
    for stroke in sess.data["strokes"]:
        add = stroke["add"]
        if add == "":
            continue
        act[add] += 1
    return (sess.data["currentUUID"], dict(tgt), act)


def count2(sess: Session) -> tuple:
    tgt = defaultdict(int)
    for key in sess.data["target"]:
        tgt[key] += 1
    act = defaultdict(int)
    for key in sess.data["text"]:
        act[key] += 1
    print(tgt, act, file=stderr)
    print(sess.data["target"], "\n" + sess.data["text"], file=stderr)
    return (sess.data["currentUUID"], dict(tgt), act)


if __name__ == "__main__":
    from sys import stdin, stdout, stderr
    from data import parse_line
    import csv

    gtgt = None
    w = csv.writer(stdout)
    for i, data in enumerate(map(count2, map(parse_line, stdin))):
        attemptID, tgt, act = data
        if i == 0:
            gtgt = tgt
            w.writerow(["attemptID"] + sorted(tgt.keys()))
            w.writerow(["target"] + [tgt[key] for key in sorted(tgt.keys())])
        elif gtgt != tgt:
            raise TypeError(f"gtgt != tgt:\ngtgt: {gtgt}\ntgt: {tgt}")
        w.writerow([attemptID] + [act[key] for key in sorted(tgt.keys())])
