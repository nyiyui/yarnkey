from dateutil import parser
import json
import datetime


class Session:
    ts: datetime.datetime = None
    data: dict = None

    def __init__(self, ts, data):
        self.ts = ts
        self.data = data

    def __str__(self):
        return self.ts.isoformat() + " " + json.dumps(self.data)


def parse_line(line: str) -> Session:
    ts, data = line.split(" ", 1)
    return Session(parser.parse(ts), json.loads(data))
