from datetime import datetime
import pandas as pd
import re

data = {
    "Platform": ["iPadOS", "macOS", "Windows", "ChromeOS"],
    "Current Live OS Version": ["17.5.1", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
    "Current Beta Releases": ["18.2 Beta, 26 Beta", "15.6 Beta, 26 Beta", "24H2 Insider Preview", ""],
    "Beta Release Date": ["2025-06-24, 2025-07-15", "2025-06-24, 2025-07-10", "2025-06", ""],
}

df = pd.DataFrame(data)

def extract_all_versions(version_str):
    if not isinstance(version_str, str) or not version_str.strip():
        return []
    parts = re.split(r"[,/;]", version_str)
    versions = []
    for part in parts:
        match = re.search(r"\d+(\.\d+)?", part)
        if match:
            versions.append(float(match.group()))
    return versions

def extract_dates(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return []
    # split dates by commas
    return [d.strip() for d in date_str.split(",")]

minor_betas = []
minor_beta_dates = []
major_betas = []
major_beta_dates = []

for idx, row in df.iterrows():
    beta_versions = extract_all_versions(row["Current Beta Releases"])
    beta_dates = extract_dates(row["Beta Release Date"])
    
    # Separate minor and major betas with dates mapped by index
    minors = []
    minors_dates = []
    majors = []
    majors_dates = []
    
    for i, v in enumerate(beta_versions):
        date = beta_dates[i] if i < len(beta_dates) else ""
        if v == int(v):
            majors.append(v)
            majors_dates.append(date)
        else:
            minors.append(v)
            minors_dates.append(date)
    
    # Get highest minor beta and its date
    if minors:
        max_minor = max(minors)
        max_minor_date = minors_dates[minors.index(max_minor)]
    else:
        max_minor = None
        max_minor_date = ""
    
    # Get highest major beta and its date
    if majors:
        max_major = max(majors)
        max_major_date = majors_dates[majors.index(max_major)]
    else:
        max_major = None
        max_major_date = ""
    
    minor_betas.append(max_minor if max_minor is not None else "")
    minor_beta_dates.append(max_minor_date)
    major_betas.append(max_major if max_major is not None else "")
    major_beta_dates.append(max_major_date)

df["Available Minor Beta OS"] = minor_betas
df["Minor Beta OS (fix) release date"] = minor_beta_dates
df["Available Major Beta OS"] = major_betas
df["Major Beta OS (new system) release date"] = major_beta_dates

df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

df.to_csv("latest_os_versions.csv", index=False)
