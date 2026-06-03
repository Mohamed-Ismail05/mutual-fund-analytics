import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Paths

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(
    f"sqlite:///{db_path}"
)

# Load CSV Files

fund_master = pd.read_csv(
    BASE_DIR / "data" / "raw" / "01_fund_master.csv"
)

nav_history = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_nav_history.csv"
)

transactions = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_investor_transactions.csv"
)

performance = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_scheme_performance.csv"
)

aum = pd.read_csv(
    BASE_DIR / "data" / "raw" / "03_aum_by_fund_house.csv"
)

monthly_sip = pd.read_csv(
    BASE_DIR / "data" / "raw" / "04_monthly_sip_inflows.csv"
)

# Load Into SQLite

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

monthly_sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

# Verifying Row Counts

print("\nRow Counts:")
print(
    "dim_fund:", len(fund_master)
)

print(
    "fact_nav:", len(nav_history)
)

print(
    "fact_transactions:", len(transactions)
)

print(
    "fact_performance:", len(performance)
)

print(
    "fact_aum:", len(aum)
)