# naplan/scrape_naplan.py

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

URL = "https://www.assessform.edu.au/naplan-online/locked-down-browser"
OUTPUT_CSV = "data/naplan_browser_versions.csv"

def fetch_versions():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n")
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    versions = []
    for line in lines:
        if "Locked down browser version" in line:
            parts = line.split(":")
            if len(parts) == 2:
                os_type = (
                    "Windows" if "Windows" in line else
                    "macOS" if "macOS" in line else
                    "Other"
                )
                versions.append((os_type, parts[1].strip()))
    return versions

def save_versions(versions):
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    file_exists = os.path.exists(OUTPUT_CSV)

    with open(OUTPUT_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "os", "version"])
        today = datetime.utcnow().date().isoformat()
        for os_type, version in versions:
            writer.writerow([today, os_type, version])

if __name__ == "__main__":
    versions = fetch_versions()
    if versions:
        save_versions(versions)
    else:
        print("No version data found!")
