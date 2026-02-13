import requests
import time


ONE_WEEK_AGO = int(time.time()) - (10 * 24 * 60 * 60)
URL = "https://hn.algolia.com/api/v1/search"

params = {
    "tags": "story",
    "numericFilters": f"created_at_i>{ONE_WEEK_AGO}",
    "hitsPerPage": 50,
    "page": 0,
    "query": ""
}

res = requests.get(URL, params=params)
data = res.json()

signals = []

for h in data["hits"]:
    title = h.get("title")
    if not title:
        continue

    title_lower = title.lower()


    points = h.get("points", 0)
    comments = h.get("num_comments", 0)

    signals.append({
        "title": title,
        "points": points,
        "comments": comments
    })

# ✅ sort using real numbers (no parsing)
signals.sort(
    key=lambda x: x["points"],
    reverse=True
)

with open("content/signals/hn.md", "w") as f:
    f.write("## Hacker News Signals (Popular – Past Week)\n\n")
    for s in signals[:10]:
        f.write(
            f"- HN: {s['title']} ({s['points']} points, {s['comments']} comments)\n"
        )