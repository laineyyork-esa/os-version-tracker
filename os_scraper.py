from datetime import datetime
import pandas as pd
import re

# Sample data (edit as needed)
data = {
    "Platform": ["iPadOS", "macOS", "Windows", "ChromeOS"],
    "Current Available Release": ["17.5.1", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Current Beta Releases": ["18.2 Beta", "15.6 Beta", "24H2 Insider Preview", ""],
    "Beta Release Date": ["2025-06-24", "2025-06-24", "2025-06", ""],
    "Upcoming Public Releases": ["26", "15.6", "24H2", ""],
    "Public Release Date": ["2025-09", "2025-09", "2025-09", ""],
    "Source_URL": [
        "https://www.apple.com/os/ipados/",
        "https://www.apple.com/macos/",
        "https://support.microsoft.com/en-us/topic/june-11-2025-kb5060842",
        "https://chromeos.dev/en/releases"
    ]
}

df = pd.DataFrame(data)

# Helper function to extract a major version number (returns float or int where possible)
def extract_numeric_version(version_str):
    if not isinstance(version_str, str) or not version_str.strip():
        return None
    # Extract the first number that looks like a version
    match = re.search(r"\d+(\.\d+)?", version_str)
    if match:
        return float(match.group())
    return None

# Compute "Highest Available Release"
highest_versions = []
for idx, row in df.iterrows():
    versions = []
    for col in ["Current Beta Releases", "Upcoming Public Releases"]:
        val = extract_numeric_version(row[col])
        if val is not None:
            versions.append(val)
    highest_versions.append(max(versions) if versions else None)

df["Highest Available Release"] = highest_versions

# Optional: Add Release Type (major if integer, minor if decimal)
def release_type(v):
    if v is None:
        return ""
    return "Major" if v == int(v) else "Minor"

df["Release Type"] = df["Highest Available Release"].apply(release_type)

# Add UTC timestamp
df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Save to CSV
df.to_csv("latest_os_versions.csv", index=False)
