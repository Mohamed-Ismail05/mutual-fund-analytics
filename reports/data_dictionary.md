## Data Dictionary
## Project Overview

This is prepared as a part of Bluestock Mutaul Fund Analysis capstone project which helps to understand the datasetsused for cleaning, Db design, Sql Analysis and dashboard.

The datas below describes the purpose of each datasets and explain the meaning.

# Dataset 1: Fund Master

Source File: 01_fund_master.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | Integer | Unique identifier assigned by AMFI to a mutual fund scheme |
| fund_house | Text | Name of the mutual fund company |
| scheme_name | Text | Name of the mutual fund scheme |
| category | Text | Broad investment category of the scheme |
| sub_category | Text | Detailed classification within a category |
| plan | Text | Indicates Direct or Regular plan |
| launch_date | Date | Date when the scheme was launched |
| benchmark | Text | Benchmark index used for performance comparison |
| expense_ratio_pct | Float | Annual expense ratio charged by the fund (%) |
| exit_load_pct | Float | Exit load applicable during redemption (%) |
| min_sip_amount | Integer | Minimum amount required for SIP investment |
| min_lumpsum_amount | Integer | Minimum lump sum investment amount |
| fund_manager | Text | Name of the fund manager |
| risk_category | Text | Risk level assigned to the scheme |
| sebi_category_code | Text | SEBI classification code |

---

# Dataset 2: NAV History

Source File: 02_nav_history.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | Integer | Scheme identifier |
| date | Date | NAV reporting date |
| nav | Float | Net Asset Value of the scheme on the given date |

---

# Dataset 3: AUM by Fund House

Source File: 03_aum_by_fund_house.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| date | Date | Reporting date |
| fund_house | Text | Mutual fund company name |
| aum_lakh_crore | Float | Assets under management in lakh crore |
| aum_crore | Integer | Assets under management in crore |
| num_schemes | Integer | Number of schemes managed by the fund house |

---

# Dataset 4: Monthly SIP Inflows

Source File: 04_monthly_sip_inflows.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| month | Text | Reporting month |
| sip_inflow_crore | Integer | Total SIP inflow during the month (₹ Crore) |
| active_sip_accounts_crore | Float | Active SIP accounts (Crore) |
| new_sip_accounts_lakh | Float | New SIP accounts opened (Lakh) |
| sip_aum_lakh_crore | Float | SIP assets under management (Lakh Crore) |
| yoy_growth_pct | Float | Year-over-year growth percentage |

---

# Dataset 5: Category Inflows

Source File: 05_category_inflows.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| month | Text | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Float | Net inflow or outflow in crore |

---

# Dataset 6: Industry Folio Count

Source File: 06_industry_folio_count.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| month | Text | Reporting month |
| total_folios_crore | Float | Total industry folios |
| equity_folios_crore | Float | Equity fund folios |
| debt_folios_crore | Float | Debt fund folios |
| hybrid_folios_crore | Float | Hybrid fund folios |
| others_folios_crore | Float | Other category folios |

---

# Dataset 7: Scheme Performance

Source File: 07_scheme_performance.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | Integer | Scheme identifier |
| scheme_name | Text | Mutual fund scheme name |
| fund_house | Text | Fund house name |
| category | Text | Scheme category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Float | One-year return (%) |
| return_3yr_pct | Float | Three-year annualized return (%) |
| return_5yr_pct | Float | Five-year annualized return (%) |
| benchmark_3yr_pct | Float | Three-year benchmark return (%) |
| alpha | Float | Risk-adjusted excess return |
| beta | Float | Sensitivity to market movements |
| sharpe_ratio | Float | Risk-adjusted return metric |
| sortino_ratio | Float | Downside-risk adjusted return metric |
| std_dev_ann_pct | Float | Annualized volatility (%) |
| max_drawdown_pct | Float | Maximum decline from peak (%) |
| aum_crore | Integer | Scheme assets under management |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| morningstar_rating | Integer | Morningstar rating score |
| risk_grade | Text | Risk classification |

---

# Dataset 8: Investor Transactions

Source File: 08_investor_transactions.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme identifier |
| transaction_type | Text | SIP, Lumpsum, or Redemption |
| amount_inr | Integer | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification of city |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income in lakh |
| payment_mode | Text | Payment channel used |
| kyc_status | Text | KYC verification status |

---

# Dataset 9: Portfolio Holdings

Source File: 09_portfolio_holdings.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | Integer | Scheme identifier |
| stock_symbol | Text | Stock market symbol |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio allocation percentage |
| market_value_cr | Float | Market value in crore |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

# Dataset 10: Benchmark Indices

Source File: 10_benchmark_indices.csv

| Column Name | Data Type | Description |
|------------|------------|------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index name |
| close_value | Float | Closing value of the benchmark index |


## Data Quality Notes

During the data cleaning phase, the NAV history dataset was checked for duplicate records, invalid values, and missing dates. Investor transaction records were validated for transaction amounts and KYC status values. Scheme performance data was reviewed to ensure return-related fields were numeric and expense ratios were within expected industry ranges.

A cross-validation was also performed between Fund Master and NAV History datasets, confirming that all AMFI scheme codes were present and matched correctly.

