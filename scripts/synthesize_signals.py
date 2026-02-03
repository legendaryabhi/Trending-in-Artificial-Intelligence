from pathlib import Path

hn = Path("content/signals/hn.md").read_text()
gh = Path("content/signals/github.md").read_text()
cl = Path("content/signals/clusters.md").read_text()

Path("content/signals/weekly-signals.md").write_text(
    "# Weekly AI Signals\n\n" + hn + "\n\n" + gh + "\n\n" + cl
)
