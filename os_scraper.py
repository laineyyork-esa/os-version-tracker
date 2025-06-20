from datetime import datetime
import pandas as pd

data = {
    "Platform": ["iPadOS", "iOS", "macOS", "Windows", "ChromeOS"],
    "Latest_Version": ["26", "26", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Next_Version": ["26 (beta)", "26 (beta)", "26 Tahoe (beta)", "", ""],
    "Descriptive_Name": ["", "", "Tahoe", "", ""],
    "Release_Date": ["2025-06-09", "2025-06-09", "2025-09 (public 2025)", "2025-06-11", "2025-06-17"],
    "Source_URL": [
        "https://www.apple.com/os/ipados/",
        "https://www.apple.com/newsroom/2025/06/apple-unveils-ios-26-at-wwdc25/",
        "https://www.apple.com/newsroom/2025/06/macos-tahoe-26-makes-the-mac-more-capable-productive-and-intelligent-than-ever/",
        "https://support.microsoft.com/en-us/topic/june-11-2025-kb5060842",
        "https://chromeos.dev/en/releases"
    ]
}

df = pd.DataFrame(data)
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
df.to_csv("latest_os_versions.csv", index=False)

