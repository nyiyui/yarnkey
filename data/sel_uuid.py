#!/bin/env python3

def match_sess(f):
    return lambda sess: f(sess.data['currentUUID'])

if __name__ == '__main__':
    from sys import stdin, argv
    from data import parse_line
    import re

    re = re.compile(argv[1])
    match = match_sess(lambda x: bool(re.match(x)))
    if len(argv) > 2:
        if argv[2] == 'exclude':
            match_old = match
            match = lambda x: not match_old(x)

    for sess in filter(match, map(parse_line, stdin)):
        print(sess)
