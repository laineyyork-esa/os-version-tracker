from datetime import datetime
import pandas as pd
import re

data = {
    "Platform": ["iPadOS", "macOS", "Windows", "ChromeOS"],
    "Current Live OS": ["17.5.1", "15.5", "22H2 Build 22631.3593", "134.0.6385.204"],
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
    return [d.strip() for d in date_str.split(",")]

bug_fix_betas = []
bug_fix_beta_dates = []
major_betas = []
major_beta_dates = []

for idx, row in df.iterrows():
    beta_versions = extract_all_versions(row["Current Beta Releases"])
    beta_dates = extract_dates(row["Beta Release Date"])
    
    bug_fix_list = []
    bug_fix_dates = []
    major_list = []
    major_dates = []
    
    for i, v in enumerate(beta_versions):
        date = beta_dates[i] if i < len(beta_dates) else ""
        if v == int(v):
            major_list.append(v)
            major_dates.append(date)
        else:
            bug_fix_list.append(v)
            bug_fix_dates.append(date)
    
    if bug_fix_list:
        max_bug_fix = max(bug_fix_list)
        max_bug_fix_date = bug_fix_dates[bug_fix_list.index(max_bug_fix)]
    else:
        max_bug_fix = ""
        max_bug_fix_date = ""
    
    if major_list:
        max_major = max(major_list)
        max_major_date = major_dates[major_list.index(max_major)]
    else:
        max_major = ""
        max_major_date = ""
    
    bug_fix_betas.append(max_bug_fix)
    bug_fix_beta_dates.append(max_bug_fix_date)
    major_betas.append(max_major)
    major_beta_dates.append(max_major_date)

df["Available Bug Fix Beta"] = bug_fix_betas
df["Bug Fix Beta Release Date"] = bug_fix_beta_dates
df["Available Major Beta OS"] = major_betas
df["Major Beta OS release date"] = major_beta_dates

df["Checked_On"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

df.to_csv("latest_os_versions.csv", index=False)
