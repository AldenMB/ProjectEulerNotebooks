import csv
import itertools
import logging
import re
from datetime import timedelta
from pathlib import Path

import nbformat
import requests
import requests_cache

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


session = requests_cache.CachedSession()
proxies = None

ROOT = "http://projecteuler.net/"

pather = re.compile(
    '<(?:a href|img src)="(?P<path>project/(?:resources/.*?_|images/)(?P<name>.*?))"'
)

destination = Path("./problems")


def _get_raw(n, session=session):
    """Return the raw text for problem n."""
    problem = session.get(ROOT + f"minimal={n}", proxies=proxies)
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
    text = text.replace(
        'class="monospace center"',
        'style="text-align: center !important; font-family: monospace"',
    )
    text = text.replace('class="center"', 'style="text-align: center !important"')
    text = text.replace('class="red"', 'style="color: red"')
    return text


def _make_nb(description, statement, number):
    link = ROOT + f"problem={number}"
    nb = nbformat.v4.new_notebook()
    nb["cells"] = [
        nbformat.v4.new_markdown_cell(
            f'# <a href="{link}">{description}</a>\n\n## Problem {number}\n\n{statement}',
            id="0",
        ),
        nbformat.v4.new_markdown_cell("# Solution\n", id="1"),
        nbformat.v4.new_code_cell(id="2"),
    ]
    return nb


def find_proxy():
    global proxies
    try:
        requests.get(ROOT).raise_for_status()
    except:
        proxy_list = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        proxy_list.raise_for_status()
        for proxy in proxy_list.iter_lines():
            p = {'http':f'http://{proxy.decode()}'}
            try:
                res = requests.get(ROOT, proxies=p, timeout = 1)
            except:
                pass
            else:
                if res.status_code == 200:
                    break
        else:
            raise ConnectionError("no usable proxy was found")
        proxies = p
    

def fetch_problem(n, description, problem_folder):
    digits = f"{n:04d}"
    destination = problem_folder / digits
    if destination.exists():
        return
    destination.mkdir()
    raw = _get_raw(n)
    statement, resources = _strip_links(raw)
    statement = _inline_format(statement)
    with open(destination / f"{digits}.ipynb", "w", encoding="utf-8") as f:
        nbformat.write(_make_nb(description, statement, n), f)
    for path, name in resources:
        res = session.get(ROOT + path)
        res.raise_for_status()
        with open(destination / name, "wb") as f:
            for chunk in res.iter_content(100_000):
                f.write(chunk)


def fetch_all(destination=destination):
    res = session.get(ROOT + "minimal=problems;csv", expire_after=0, proxies=proxies)
    logger.debug(res.request.headers)
    logger.debug(res.request.url)
    logger.debug(res.request.body)
    logger.debug(res.status_code)
    logger.debug(res.reason)
    res.raise_for_status()
    reader = csv.reader(res.text.splitlines())
    for id_num, description, published, solved_by in itertools.islice(reader, 1, None):
        fetch_problem(int(id_num), description, destination)


def upcoming():
    res = session.get(ROOT + "minimal=new", expire_after=0, proxies=proxies)
    res.raise_for_status()
    return res.text
