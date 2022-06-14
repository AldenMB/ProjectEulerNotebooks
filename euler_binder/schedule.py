import datetime
import re
from pathlib import Path

from .fetch import upcoming

record = Path("./.github/workflows/fetch.yml")


def to_cron(dt):
    return f"    - cron: '{dt.minute} {dt.hour} {dt.day} {dt.month} *'"


def schedule():
    stamps = (line.split("##")[1] for line in upcoming().splitlines())
    dts = (datetime.datetime.fromtimestamp(int(stamp)) for stamp in stamps)
    margin = datetime.timedelta(minutes=5)
    crons = [to_cron(dt + margin) for dt in dts]
    if len(crons) < 1:
        crons = ["    - cron: '3 2 1 * *'"]
    new_crons = "\n" + "\n".join(crons) + "\n"

    with open(record, "r") as f:
        new_file = re.sub(r"(\n?    - cron: '.*?'\n)+", new_crons, f.read())

    with open(record, "w") as f:
        f.write(new_file)
