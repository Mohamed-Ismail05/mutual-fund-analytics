import requests
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in funds.items():
    try:
        url = f"https://api.mfapi.in/mf/{amfi_code}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = RAW_DIR / f"{fund_name}_live_nav.csv"
        nav_df.to_csv(output_file, index=False)

        print(f"✓ Saved {fund_name}")

    except Exception as e:
        print(f"✗ Error fetching {fund_name}: {e}")