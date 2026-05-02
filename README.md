# Sales & Profitability Analysis 

**Dataset:** This analysis utilizes the [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) from Kaggle, which provides comprehensive data on sales, profits, and customer segments.

This repository contains a data analysis project focused on understanding sales performance and profitability drivers. The analysis is performed using Python, Pandas and statsmodels on a retail dataset.


## Key Business Insights / Results

### The 20% Discount Tipping Point
- Our analysis shows a direct negative correlation between discounts and profitability. Transactions with discounts exceeding 20% are statistically likely to result in a net loss. (See the jitter plot below)

![Discount vs Profit margin](outputs/Discount_vs_Profit_margin_jitter.png)


### Strategic Recommendations
- **Pricing:** Require managerial approval for any discounts exceeding 20%.
- **Inventory Focus:** Prioritize **Technology** and **Office Supplies**, which show significantly higher margin efficiency than Furniture.
- **Volume vs. Profit:** Disprove the "volume fixes everything" myth; quantity sold does not statistically improve the profit margin (p > 0.05).


## Project Overview
The goal of this project is to identify which product categories, customer segments, and regional markets contribute most to the company's bottom line, as well as to evaluate the impact of discounting strategies.


### 1. Regional Analysis
Analyze profitability and sales across different geographical regions.
- Identifying the most profitable states while marking states with negative profit with red color. 

![Regional Profitability](outputs/Regional_profitability.png)


### 2. Customer Segments & Category Profitability
Investigating how sales and profits are distributed across different customer segments (Consumer, Corporate, Home office).
Analyze which products and categories generate the highest sales and profit.
- Sorting sub-categories by profit within each parent category to identify top performers and loss-makers.

![Product Performance](outputs/Product_performance.png)


### 3. Discount Impact Analysis
Evaluating whether discounting strategies increase or decrease profit
- Effect of discount on profit margin

![Discount vs Profit margin](outputs/Discount_vs_Profit_margin_jitter.png)


### Linear regression: Factors Driving Profit Margin

Performed a Multiple Linear Regression (OLS) to identify key drivers of profitability. $$\text{Profit Margin} \sim \text{Quantity} + \text{Discount} + \text{Segment} + \text{Category} + \text{Region}$$ The model achieved an **R-squared** of 0.756.

- **Key Insight:** Discounting is the strongest predictor of loss. A 10% increase in discount leads to a ~**19%** drop in profit margin.

- **Category Performance:** Office Supplies and Technology outperform Furniture in terms of margin efficiency.

- **Statistical Discovery:** Order quantity does not have a statistically significant impact on the profit margin (p = 0.735), suggesting that scaling volume doesn't fix poor pricing strategies.


## Tech Stack
- **Python** 3.12.6
- **Libraries:** Pandas (Data manipulation), Matplotlib / Seaborn (visualization), statsmodels (statistical modeling)
- **Power BI** (Interactive dashboard, Geospatial Analysis, DAX) 
- **Environment:** Jupyter Notebook