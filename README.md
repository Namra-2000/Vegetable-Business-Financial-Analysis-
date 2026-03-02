# 📊 Analytical Study of a Wholesale & Retail Vegetable Seller


## 👤 Student Details

| Field | Details |
|---|---|
| **Name** | Namra Sania |
| **Roll Number** | 23f2000313 |
| **Program** | IITM Online BS Degree Program |


---

## 🏪 Business Details

| Field | Details |
|---|---|
| **Business Name** | Raj Kishore Gupta and Sons |
| **Location** | Mubarakpur Sabji Mandi, Mubarakpur, Azamgarh, Uttar Pradesh |
| **Owner** | Mr. Raj Kishore Gupta |
| **Type** | Wholesale & Retail Vegetable Seller (B2B + B2C) |
| **Experience** | 20+ Years |

---

## 📌 Project Title
**"Navigating Financial Obstacles: Leveraging Data in Vegetable Business"**

---

## 🎯 Problem Statements

### Problem 1 — No Financial Clarity
The business owner had no system to track daily profits, required turnover, or appropriate
pricing margins needed to achieve a desired monthly income.

### Problem 2 — No Structured Credit System
Credit was extended to wholesale customers without any fixed criteria, cap on outstanding
dues, or structured repayment schedule — creating financial risk.

---

## 📁 Repository Structure

```
BDM_Project/
│
├── data/
│   ├── vegetable_transactions.csv     # Daily per-vegetable transaction data (Jan 16 – Feb 15, 2024)
│   ├── daily_summary.csv              # Daily aggregated financial summary
│   └── credit_data.csv               # Credit & repayment data for 6 customers
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb         # Data cleaning and preprocessing
│   ├── 02_financial_analysis.ipynb    # Revenue, cost, profit analysis
│   ├── 03_margin_analysis.ipynb       # Margin analysis + linear regression
│   └── 04_credit_analysis.ipynb       # Credit customer analysis
│
├── src/
│   └── analysis.py                   # Core analysis functions
│
├── reports/
│   ├── Proposal_Report.pdf           # Project proposal
│   ├── MidTerm_Report.pdf            # Mid-term report
│   └── Final_Report.pdf              # End-term final report
│
├── dashboards/
│   └── dashboard_screenshots/        # Power BI dashboard screenshots
│
└── README.md
```

---

## 🗓️ Data Collection

- **Period:** January 16, 2024 to February 15, 2024 (31 days)
- **Business Closed:** January 26 & 27, 2024 (Republic Day)
- **Data Source:** Primary — collected directly from the business owner
- **Recording Methods Used by Owner:**
  - Laal Khata Book (detailed vegetable records)
  - Daily Notepad (purchase quantities)
  - WhatsApp Messages (credit/repayment communication)
- **Currency:** Indian Rupee (₹)

---

## 📊 Datasets

### 1. `vegetable_transactions.csv`
Per-vegetable transaction records for each business day.

| Column | Description |
|---|---|
| Date | Transaction date |
| Vegetable_Name | Name of vegetable |
| Cost_Price_per_kg | Purchase price from mandi (₹/kg) |
| Sell_Price_per_kg | Selling price to customers (₹/kg) |
| Quantity_kg | Total quantity sold (kg) |
| Margin_per_kg | SP - CP (₹/kg) |
| Pct_Margin | (Margin / CP) × 100 |

### 2. `daily_summary.csv`
Aggregated daily financial overview.

| Column | Description |
|---|---|
| Date | Business date |
| Vegetables_Cost | Total procurement cost for the day |
| Sell_with_Margin | Total selling value (60% of stock) |
| Revenue | (0.4 × Veg Cost) + (0.6 × Sell with Margin) |
| Other_Cost | Transportation + storage (₹800 Jan / ₹850 Feb) |
| Profit | Revenue − Vegetables Cost − Other Cost |
| Pct_Margin | Average % margin across all vegetables |
| Business_Open | Yes / No |

**Revenue Formula:**
```
Revenue = (40/100) × Vegetable_Cost + (60/100) × Sell_with_Margin
Profit  = Revenue − Vegetable_Cost − Other_Cost
```
> The owner sells 60% of stock at margin price (5am–12pm) and clears remaining 40% at cost price.

### 3. `credit_data.csv`
Daily credit and repayment transactions for 6 wholesale customers.

| Column | Description |
|---|---|
| Customer_Name | Name of credit customer |
| Transaction_Date | Date of transaction |
| Credit_Amount | Amount credited on that day (₹) |
| Repayment | Amount repaid on that day (₹) |
| Outstanding_Balance | Running balance owed (₹) |

---

## 🔍 Analysis Methods

| Method | Purpose |
|---|---|
| **Descriptive Statistics** | Mean, median, std dev of profit, cost, revenue |
| **Time-Series Analysis** | Trend analysis of daily profit, cost, margin over 31 days |
| **Linear Regression (Python)** | Find ideal % margin to achieve target daily profit |
| **Correlation Analysis** | Relationship between variety of vegetables and profit |
| **Credit Analysis** | Earnings per customer accounting for interest cost |
| **Spreadsheet Calculations** | Daily aggregations, KPI computations |

---

## 📈 Key Results & Findings

### Financial Overview
| Metric | Value |
|---|---|
| Mean Daily Vegetable Cost | ₹13,161 |
| Mean Daily Revenue | ₹15,233 |
| Mean Daily Profit | ₹1,246 |
| Min Daily Profit | ₹914 |
| Max Daily Profit | ₹1,963 (Jan 25 — Republic Day eve rush) |
| Total Monthly Profit | ₹36,146 |
| January Avg Profit | ₹1,339 |
| February Avg Profit | ₹1,159 |

### Margin Analysis
- **Correlation (% Margin vs Profit):** 0.689 — moderately strong positive relationship
- **Correlation (Variety vs Profit):** 0.651 — more vegetable types = higher profit
- **Ideal Margin:** 35% → **₹1,419 daily profit** → ₹37,800–40,600/month

### Ideal Margin Per Vegetable
| Vegetable | Ideal Margin (₹/kg) |
|---|---|
| Red/Yellow Capsicum | ₹30 |
| Mushroom | ₹20 |
| Arvi | ₹18.75 |
| Mongra | ₹17.5 |
| Babycorn / Green Capsicum | ₹16.25 |
| Permal-Calcutta | ₹13.75 |
| Ladyfinger | ₹12.25 |
| Cucumber-Hybrid | ₹11.5 |
| Turnip | ₹11.25 |
| China Cucumber | ₹11 |
| Lemon | ₹10.5 |
| Gooseberry | ₹10.25 |
| Gajar | ₹10 |
| Beetroot | ₹9.5 |
| Peas | ₹7.75 |

### Credit Analysis (at 35% margin, 4% interest rate)
| Customer | Total Credit | Total Repayment | Earnings |
|---|---|---|---|
| Rahul Rajora | ₹21,870 | ₹22,980 | ₹4,827 ✅ |
| Bajarangi | ₹17,520 | ₹17,080 | ₹2,538 ✅ |
| Sonu Madipur | ₹27,960 | ₹26,080 | ₹2,873 ✅ |
| **Kishore** | **₹35,860** | **₹29,400** | **−₹363 ❌** |
| Anand | ₹33,560 | ₹34,060 | ₹6,205 ✅ |
| Vanu | ₹15,940 | ₹17,540 | ₹4,309 ✅ |

> **Kishore** had skipped repayments Feb 6–14, causing an outstanding balance spike and net loss.

---

## 💡 Recommendations

1. **Maintain 35% average margin** across vegetables daily to hit ₹37,800–40,600/month income target
2. **Increase vegetable variety** — correlation of 0.65 shows more variety = more profit; add specialty items like Red/Yellow Capsicum (₹30 margin)
3. **Implement credit cap** — set a maximum outstanding balance per customer before stopping further credit
4. **Enforce repayment schedule** — fixed due dates, reminders, penalties for late payment
5. **Use accounting app** — replace Laal Khata + WhatsApp with a digital tracking system

---

## 🛠️ Tools & Technologies

| Tool | Usage |
|---|---|
| Python (Pandas, NumPy, Matplotlib, Seaborn) | EDA, statistics, linear regression, visualizations |
| PostgreSQL | Data querying, calculated columns |
| Excel / Google Sheets | Data cleaning, daily calculations, dashboards |
| Power BI (DAX, Power Query) | KPI dashboards, heatmaps, Pareto charts, time-series |

---

## 🚀 How to Run the Notebooks

```bash
# Clone the repository
git clone https://github.com/Namra-2000/BDM-Vegetable-Business-Analysis.git
cd BDM-Vegetable-Business-Analysis

# Install required Python libraries
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# Launch Jupyter
jupyter notebook

# Open notebooks in order:
# 01_data_cleaning.ipynb
# 02_financial_analysis.ipynb
# 03_margin_analysis.ipynb
# 04_credit_analysis.ipynb
```

---

## 📜 Declaration

This project was submitted as part of my coursework for the IITM Online BS Degree Program.
All data was collected from primary sources with the knowledge and consent of the business owner.
The analysis and recommendations are for academic purposes only.

**Namra Sania | Roll No: 23f2000313**


---
*© 2024 Namra Sania — IIT Madras
