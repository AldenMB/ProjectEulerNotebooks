import csv
from datetime import timedelta
import itertools
from pathlib import Path
import re

import nbformat
from requests_cache import CachedSession

session = CachedSession()


ROOT = "https://projecteuler.net/"

pather = re.compile(
    '<(?:a href|img src)="(?P<path>project/(?:resources/.*?_|images/)(?P<name>.*?))"'
)

destination = Path('./problems')

def _get_raw(n, session=session):
    """Return the raw text for problem n."""
    problem = session.get(ROOT + f"minimal={n}")
    problem.raise_for_status()
    return problem.text


def _strip_links(text):
    resources = []
    for match in pather.finditer(text):
        path = match.group("path")
        name = match.group("name")
        resources.append((path, name))
        text = text.replace(path, name)
    return text, resources


def _inline_format(text):
    text = text.replace('class="monospace center"', 'style="text-align: center !important; font-family: monospace"')
    text = text.replace('class="center"', 'style="text-align: center !important"')
    text = text.replace('class="red"', 'style="color: red"')
    return text


def _make_nb(description, statement, number):
    link = ROOT + f'problem={number}'
    nb = nbformat.v4.new_notebook()
    nb["cells"] = [
        nbformat.v4.new_markdown_cell(f'# <a href="{link}">{description}</a>\n\n## Problem {number}\n\n{statement}', id='0'),
        nbformat.v4.new_markdown_cell("# Solution\n", id='1'),
        nbformat.v4.new_code_cell(id='2'),
    ]
    return nb


def fetch_problem(n, description, problem_folder):
    digits = f"{n:04d}"
    destination = problem_folder / digits
    if destination.exists():
        return
    destination.mkdir()
    raw = _get_raw(n)
    statement, resources = _strip_links(raw)
    statement = _inline_format(statement)
    with open(destination / f"{digits}.ipynb", "w", encoding='utf-8') as f:
        nbformat.write(_make_nb(description, statement, n), f)
    for path, name in resources:
        res = session.get(ROOT + path)
        res.raise_for_status()
        with open(destination / name, "wb") as f:
            for chunk in res.iter_content(100_000):
                f.write(chunk)

def fetch_all(destination=destination):
    res = session.get(ROOT + "minimal=problems;csv", expire_after=timedelta(days=1))
    res.raise_for_status()
    reader = csv.reader(res.text.splitlines())
    for id_num, description, published, solved_by in itertools.islice(reader, 1,  None):
        fetch_problem(int(id_num), description, destination)
        
def upcoming():
    res = session.get(fetch.ROOT + "minimal=new", expire_after=timedelta(days=1))
    res.raise_for_status()
    return res.text