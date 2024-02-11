"""
Utility script to generate the list of external URLs.
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup


def get_html_files():
    return sorted(list(Path(".").glob("**/*.html")))


def get_external_links(html_file, exclude=[]):
    links = set()
    with open(html_file, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        for link in soup.find_all("a"):
            url = link.get("href")
            if url and url.startswith("http") and not any(_ in url for _ in exclude):
                links.add(url)
    return sorted(list(links))


def domain_url(url):
    domain = url.split("/")[2]
    if len(domain.split(".")) > 2:
        domain = ".".join(domain.split(".")[1:])
    return (domain, url)  # sort by domain, then by full url


if __name__ == "__main__":
    links = set()
    for html_file in get_html_files():
        for link in get_external_links(html_file, exclude=["github"]):
            links.add(link)

    links = sorted(list(links), key=domain_url)
    print("\n".join(links))
