trial_urls = [
    "http://google.com",
    "http://httpbin.org",
    "http://projecteuler.chat",
    "http://mathschallenge.net",
    "http://projecteuler.net",
    "https://projecteuler.net",
]

def try_fetching_stuff():
    from requests import get
    for url in trial_urls:
        res = get(url)
        req = res.request
        print(f"url {url} gave response {res.status_code} with reason {res.reason}. The request was for {req.url}, sending content {req.body} and headers {req.headers}")


if __name__ == "__main__":
    from .fetch import fetch_all, find_proxy
    from .schedule import schedule

    #try_fetching_stuff()
    find_proxy()
    fetch_all()
    schedule()
