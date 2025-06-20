from datetime import datetime
import pandas as pd

data = {
    "Platform": ["macOS", "iPadOS", "Windows", "ChromeOS"],
    "Latest_Version": ["15.5", "18.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Release_Date": ["2025-06-10", "2025-06-10", "2025-06-11", "2025-06-17"],
    "Source_URL": [
        "https://support.apple.com/en-us/100100",
        "https://support.apple.com/en-us/100100",
        "https://support.microsoft.com/en-us/topic/june-11-2025-kb5060842",
        "https://chromeos.dev/en/releases"
    ]
}

df = pd.DataFrame(data)
df["Checked_On"] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
df.to_csv("latest_os_versions.csv", index=False)
