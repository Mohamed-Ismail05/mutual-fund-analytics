-- Query 1: Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV by Month

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3: SIP YoY Growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
WHERE yoy_growth_pct IS NOT NULL
ORDER BY yoy_growth_pct DESC;


-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- Query 5: Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- Query 6: Top Performing Funds Based on Sharpe Ratio

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- Query 7: Most Popular Investment Category

SELECT
    category,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY category
ORDER BY total_schemes DESC;


-- Query 8: Investor Income Group Contribution

SELECT
    age_group,
    ROUND(AVG(amount_inr), 2) AS avg_investment,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY age_group
ORDER BY total_investment DESC;


-- Query 9: Fund Houses with Highest Average Returns

SELECT
    fund_house,
    ROUND(AVG(return_3yr_pct), 2) AS avg_3yr_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_3yr_return DESC;


-- Query 10: Risk vs Return Analysis

SELECT
    risk_grade,
    ROUND(AVG(return_3yr_pct), 2) AS avg_return,
    ROUND(AVG(std_dev_ann_pct), 2) AS avg_volatility
FROM fact_performance
GROUP BY risk_grade
ORDER BY avg_return DESC;