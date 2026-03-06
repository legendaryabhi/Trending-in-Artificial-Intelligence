from pathlib import Path

texts = []
files = ["content/signals/hn.md", "content/signals/github.md"]

for f in files:
    texts.extend(Path(f).read_text().lower().splitlines())

clusters = {
    "AI Agents / Dev Tools": ["agent", "cli", "ide", "copilot"],
    "AI Models / Infra": ["model", "training", "inference"],
    "AI Society / Impact": ["impact", "future", "skills"]
}

results = {k: [] for k in clusters}

for line in texts:
    for cluster, keys in clusters.items():
        if any(k in line for k in keys):
            results[cluster].append(line)

out = Path("content/signals/clusters.md")
out.write_text("## Detected Trend Clusters\n\n")

for cluster, items in results.items():
    if len(items) >= 2:
        out.write_text(
            out.read_text() +
            f"### {cluster}\n" +
            "\n".join(f"- {i}" for i in items[:4]) +
            "\n\n"
        )
