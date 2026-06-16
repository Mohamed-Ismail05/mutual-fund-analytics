# DAY 6 - TASK 5
# Simple Mutual Fund Recommendation Engine

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
fund_data = pd.read_csv(PROJECT_ROOT / "data" / "processed" / "clean_scheme_performance.csv")

def recommend_funds(risk_appetite):

    risk_mapping = {"Low": ["Low"],"Moderate": ["Moderate"],"High": ["High"]}
    if risk_appetite not in risk_mapping:
        print("Invalid risk appetite. Choose: ""Low, Moderate or High.")
        return None
    eligible_funds = (fund_data[fund_data["risk_grade"].isin(risk_mapping[risk_appetite])].copy())
    recommendations = (eligible_funds.sort_values(by="sharpe_ratio",ascending=False).head(3))
    return recommendations[[
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "aum_crore"]
    ]

user_risk = input("Enter Risk Appetite ""(Low / Moderate / High): ")
result = recommend_funds(user_risk)

if result is not None:

    print("\nTop Fund Recommendations\n")
    print(result.to_string(index=False))