SELECT COUNT(*) AS total_customers
FROM customers;
SELECT Churn, COUNT(*) AS customer_count
FROM customers
GROUP BY Churn;
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS churn_percentage
FROM customers
GROUP BY Contract;
SELECT
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    Churn
FROM customers
ORDER BY MonthlyCharges DESC
LIMIT 10;
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS churn_percentage
FROM customers
GROUP BY InternetService
ORDER BY churn_percentage DESC;
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE 'Above 48 Months'
    END AS customer_segment,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customers
GROUP BY customer_segment
ORDER BY total_customers DESC;
SELECT
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    InternetService,
    Churn
FROM customers
WHERE Contract = 'Month-to-month'
AND tenure <= 12
AND MonthlyCharges > 70
ORDER BY MonthlyCharges DESC;