trial_urls = [
    "https://google.com",
    "https://httpbin.org",
    "https://projecteuler.chat",
    "https://mathschallenge.net",
    "https://projecteuler.net",
    "https://projecteuler.net/problem=1",
    "https://projecteuler.net/minimal=1",
    "https://projecteuler.net/minimal=problems",
    "https://projecteuler.net/minimal=problems;csv",
]

def try_fetching_stuff():
    from requests import get
    for url in trial_urls:
        res = get(url)
        req = res.request
        print(f"url {url} gave response {res.status_code} with reason {res.reason}. The request was for {req.url}, sending content {req.body} and headers {req.headers}")


if __name__ == "__main__":
    from .fetch import fetch_all
    from .schedule import schedule

    try_fetching_stuff()

    fetch_all()
    schedule()
