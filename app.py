import requests
from rich import print

r = requests.get("https://example.com", timeout=10)
print(f"[green]Status:[/green] {r.status_code}")
