from datetime import datetime
import pandas as pd

data = {
    "Platform": ["iPadOS", "iOS", "macOS", "Windows", "ChromeOS"],
    "Current_Release": ["17.5.1", "17.5.1", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Upcoming_Release": ["26", "26", "26.0", "", ""],
    "Upcoming_Release_Date": ["2025-09", "2025-09", "2025-09", "", ""],
    "Descriptive_Name": ["", "", "Tahoe", "", ""],
    "Source_URL": [
        "https://www.apple.com/os/ipados/",
        "https://www.apple.com/ios/",
        "https://www.apple.com/macos/",
        "https://support.microsoft.com/en-us/topic/june-11-2025-kb5060842",
        "https://chromeos.dev/en/releases"
    ]
}

df = pd.DataFrame(data)
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
df.to_csv("latest_os_versions.csv", index=False)
