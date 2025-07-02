from datetime import datetime
import pandas as pd

data = {
    "Platform": ["iPadOS", "iOS", "macOS", "Windows", "ChromeOS"],
    "Current_Available_Release": ["17.5.1", "17.5.1", "15.5", "24H2 Build 22631.3593", "139.0.0"],
    "Current_Beta_Releases": [
        "iPadOS 26 Beta 2 (23A5276F)", 
        "iOS 26 Beta 2 (23A5276F)", 
        "macOS 26 Beta 2 (23A5276F)", 
        "Windows 24H2 Beta (Build 22631.3593)", 
        "ChromeOS 142 Beta (Released 1st Oct)"
    ],
    "Upcoming_Public_Releases": ["26", "26", "26.0", "", "142"],
    "Upcoming_Release_Date": ["2025-09", "2025-09", "2025-09", "", "2025-08-05"],
    "Beta_Developer_Release_Date": [  # New column added here
        "2025-06-10",  # Example date for iPadOS
        "2025-06-10",  # Example date for iOS
        "2025-06-10",  # Example date for macOS
        "2025-06-12",  # Example for Windows beta
        "2025-10-01"   # Date listed in beta description for ChromeOS
    ],
    "Source_URL": [
        "https://developer.apple.com/news/releases/",
        "https://developer.apple.com/news/releases/",
        "https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26-release-notes",
        "https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information",
        "https://chromiumdash.appspot.com/schedule"
    ]
}

df = pd.DataFrame(data)
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
df.to_csv("latest_os_versions.csv", index=False)
