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
        "ChromeOS 142 Beta (Released 1st Oct)"  # Added ChromeOS Beta details
    ],
    "Upcoming_Public_Releases": ["26", "26", "26.0", "", "142"],  # ChromeOS 142 is the upcoming release
    "Upcoming_Release_Date": ["2025-09", "2025-09", "2025-09", "", "2025-08-05"],  # ChromeOS 142 public release date
    "Source_URL": [
        "https://developer.apple.com/news/releases/",  # Updated iPadOS/iOS/macOS URLs
        "https://developer.apple.com/news/releases/",  # Updated iPadOS/iOS/macOS URLs
        "https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26-release-notes",  # iOS 26 specific
        "https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information",  # Windows 24H2
        "https://chromiumdash.appspot.com/schedule"  # ChromeOS release schedule
    ]
}

df = pd.DataFrame(data)
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")  # Timestamp for when the data was checked
df.to_csv("latest_os_versions.csv", index=False)  # Saving the updated CSV
