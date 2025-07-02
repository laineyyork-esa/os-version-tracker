from datetime import datetime
import pandas as pd

data = {
    "Platform": ["iPadOS", "macOS", "Windows", "ChromeOS"],
    "Current Available Release": ["17.5.1", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Current Beta Releases": ["18 Developer Beta 2", "15.6 Beta", "24H2 Insider Preview", ""],
    "Beta Release Date": ["2025-06-24", "2025-06-24", "2025-06", ""],
    "Upcoming Public Releases": ["18", "15.6", "24H2", ""],
    "Public Release Date": ["2025-09", "2025-09", "2025-09", ""],
    "Source_URL": [
        "https://www.apple.com/os/ipados/",
        "https://www.apple.com/macos/",
        "https://support.microsoft.com/en-us/topic/june-11-2025-kb5060842",
        "https://chromeos.dev/en/releases"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add timestamp
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Save to CSV
df.to_csv("latest_os_versions.csv", index=False)
