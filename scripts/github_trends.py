import requests
from bs4 import BeautifulSoup

URL = "https://github.com/trending?since=weekly"
html = requests.get(URL).text
soup = BeautifulSoup(html, "html.parser")

KEYWORDS = ["ai", "agent", "llm", "automation", "ide", "cli"]

signals = []

for item in soup.select("article.Box-row"):
    name = item.select_one("h2 a").text.strip().replace("\n", "")
    desc_el = item.select_one("p")
    desc = desc_el.text.strip().lower() if desc_el else ""

    if any(k in desc for k in KEYWORDS):
        signals.append(f"- GitHub Trending: {name} — {desc[:120]}")

with open("content/signals/github.md", "w") as f:
    f.write("## GitHub Trending Signals\n\n")
    f.write("\n".join(signals[:10]))
