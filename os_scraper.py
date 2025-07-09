import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_apple_releases():
    url = "https://developer.apple.com/news/releases/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    releases = soup.find_all("li")
    data = []
    for release in releases:
        text = release.get_text(strip=True)
        if "iPadOS" in text or "macOS" in text:
            data.append({
                "Platform": "iPadOS" if "iPadOS" in text else "macOS",
                "Release": text,
                "Date": datetime.today().strftime("%Y-%m-%d")
            })
    return data

def fetch_chromebook_schedule():
    url = "https://chromiumdash.appspot.com/fetch_schedule"
    response = requests.get(url)
    schedule = response.json()
    data = []
    for item in schedule:
        if item.get("milestone"):
            data.append({
                "Platform": "ChromeOS",
                "Release": f"Milestone {item['milestone']}",
                "Date": item.get("stable_date", "Unknown")
            })
    return data

def scrape_windows_releases():
    url = "https://learn.microsoft.com/en-us/windows/release-health/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    updates = soup.find_all("li")
    data = []
    for update in updates:
        text = update.get_text(strip=True)
        if "Windows 11" in text or "Windows 10" in text:
            data.append({
                "Platform": "Windows",
                "Release": text,
                "Date": datetime.today().strftime("%Y-%m-%d")
            })
    return data

def compile_os_updates():
    all_data = []
    all_data.extend(scrape_apple_releases())
    all_data.extend(fetch_chromebook_schedule())
    all_data.extend(scrape_windows_releases())
    df = pd.DataFrame(all_data)
    df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    df.to_csv("daily_os_updates.csv", index=False)
    print("✅ OS update data saved to daily_os_updates.csv")

if __name__ == "__main__":
    compile_os_updates()
