"""
BDM Capstone Project — Core Analysis Functions
Analytical Study of a Wholesale & Retail Vegetable Seller

Student  : Namra Sania
Roll No  : 23f2000313
Institute: IIT Madras Online BS Degree Program
Business : Raj Kishore Gupta and Sons, Mubarakpur, Azamgarh, Uttar Pradesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# ─────────────────────────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────────────────────────

def load_data():
    """Load all three datasets."""
    veg   = pd.read_csv('../data/vegetable_transactions.csv', parse_dates=['Date'], dayfirst=True)
    daily = pd.read_csv('../data/daily_summary.csv',          parse_dates=['Date'], dayfirst=True)
    credit= pd.read_csv('../data/credit_data.csv',            parse_dates=['Transaction_Date'], dayfirst=True)
    return veg, daily, credit


# ─────────────────────────────────────────────────────────────────
# FINANCIAL CALCULATIONS
# ─────────────────────────────────────────────────────────────────

def calculate_revenue(veg_cost, sell_with_margin):
    """
    Revenue = (40/100) * Vegetable_Cost + (60/100) * Sell_with_Margin
    60% of stock sold at margin price, 40% cleared at cost price.
    """
    return (0.40 * veg_cost) + (0.60 * sell_with_margin)


def calculate_profit(revenue, veg_cost, other_cost):
    """Profit = Revenue - Vegetable_Cost - Other_Cost"""
    return revenue - veg_cost - other_cost


def calculate_margin(cp, sp):
    """Margin per kg = SP - CP"""
    return sp - cp


def calculate_pct_margin(cp, sp):
    """% Margin = (SP - CP) / CP * 100"""
    return ((sp - cp) / cp) * 100


# ─────────────────────────────────────────────────────────────────
# FINANCIAL OVERVIEW
# ─────────────────────────────────────────────────────────────────

def financial_overview(daily_df):
    """Print full financial overview of the business."""
    open_days = daily_df[daily_df['Business_Open'] == 'Yes'].copy()

    print("=" * 55)
    print("   FINANCIAL OVERVIEW — RAJ KISHORE GUPTA & SONS")
    print("   Mubarakpur, Azamgarh, Uttar Pradesh")
    print("=" * 55)
    print(f"\n📅 Period        : Jan 16 – Feb 15, 2024 ({len(daily_df)} days total)")
    print(f"🏪 Business Days : {len(open_days)} open | 2 closed (Jan 26-27)")
    print(f"\n💰 REVENUE & COST")
    print(f"   Mean Vegetable Cost  : ₹{open_days['Vegetables_Cost'].mean():,.2f}")
    print(f"   Mean Revenue         : ₹{open_days['Revenue'].mean():,.2f}")
    print(f"   Other Costs (Jan)    : ₹800  |  (Feb) ₹850")
    print(f"\n📈 PROFIT ANALYSIS")
    print(f"   Mean Daily Profit    : ₹{open_days['Profit'].mean():,.2f}")
    print(f"   Median Daily Profit  : ₹{open_days['Profit'].median():,.2f}")
    print(f"   Std Dev              : ₹{open_days['Profit'].std():,.2f}")
    print(f"   Min Daily Profit     : ₹{open_days['Profit'].min():,.2f}")
    print(f"   Max Daily Profit     : ₹{open_days['Profit'].max():,.2f}")
    print(f"   Total Monthly Profit : ₹{open_days['Profit'].sum():,.2f}")

    jan = open_days[open_days['Date'].dt.month == 1]['Profit'].mean()
    feb = open_days[open_days['Date'].dt.month == 2]['Profit'].mean()
    print(f"\n📅 MONTHLY COMPARISON")
    print(f"   Jan Avg Profit : ₹{jan:,.2f}")
    print(f"   Feb Avg Profit : ₹{feb:,.2f}")
    print("=" * 55)
    return open_days


# ─────────────────────────────────────────────────────────────────
# MARGIN ANALYSIS
# ─────────────────────────────────────────────────────────────────

def margin_regression(daily_df):
    """
    Linear regression: % Margin vs Profit
    Find the margin % required to achieve target profit.
    """
    df = daily_df[(daily_df['Profit'] != 0) & (daily_df['Pct_Margin'] != 0)].copy()

    X = df[['Pct_Margin']].values
    y = df['Profit'].values

    model = LinearRegression()
    model.fit(X, y)

    slope     = model.coef_[0]
    intercept = model.intercept_
    r2        = model.score(X, y)
    corr      = df['Pct_Margin'].corr(df['Profit'])

    target_margin = 35
    predicted_profit = slope * target_margin + intercept

    print("\n📊 MARGIN REGRESSION ANALYSIS")
    print(f"   Slope              : {slope:.4f}")
    print(f"   Intercept          : {intercept:.4f}")
    print(f"   R² Score           : {r2:.4f}")
    print(f"   Correlation        : {corr:.4f}")
    print(f"   Profit @ 35% margin: ₹{predicted_profit:,.2f}")
    print(f"   Monthly (×29 days) : ₹{predicted_profit*29:,.0f} – ₹{predicted_profit*29*1.02:,.0f}")

    return model, slope, intercept, corr


def variety_profit_correlation(daily_df):
    """Correlation between number of vegetable varieties sold and profit."""
    df = daily_df[daily_df['Business_Open'] == 'Yes']
    corr = df['No_of_Vegetables_Sold'].corr(df['Profit'])
    print(f"\n🥦 Variety vs Profit Correlation: {corr:.4f}")
    print(f"   → More varieties = {'Higher' if corr > 0 else 'Lower'} profit (moderately strong)")
    return corr


def ideal_margins_per_vegetable(veg_df, daily_df, margin_range=(34, 36)):
    """
    Filter days where overall % margin is within ideal range,
    then compute average margin per vegetable on those days.
    """
    good_days = daily_df[
        (daily_df['Pct_Margin'] >= margin_range[0]) &
        (daily_df['Pct_Margin'] <= margin_range[1])
    ]['Date'].tolist()

    filtered = veg_df[veg_df['Date'].isin(good_days)]
    ideal = filtered.groupby('Vegetable_Name')['Margin_per_kg'].mean().round(2).sort_values(ascending=False)

    print(f"\n🎯 IDEAL MARGINS (days with {margin_range[0]}–{margin_range[1]}% overall margin)")
    for veg, margin in ideal.items():
        print(f"   {veg:<25} ₹{margin}")
    return ideal


# ─────────────────────────────────────────────────────────────────
# CREDIT ANALYSIS
# ─────────────────────────────────────────────────────────────────

def credit_summary(credit_df, margin_pct=35, interest_rate=4):
    """
    Compute per-customer credit summary and earnings.

    Earnings = Total_Repayment + Profit - Total_Credit - Interest_Cost
    Profit   = (margin_pct/100) * (60/100) * Total_Credit
    Interest = (interest_rate/100) * Total_Credit
    """
    # Exclude opening balance rows
    txn = credit_df[credit_df['Transaction_Date'] != '2024-01-15'].copy()

    summary = txn.groupby('Customer_Name').agg(
        Total_Credit    = ('Credit_Amount', 'sum'),
        Total_Repayment = ('Repayment', 'sum')
    ).reset_index()

    summary['Interest_Cost'] = (interest_rate / 100) * summary['Total_Credit']
    summary['Profit_on_Credit'] = (margin_pct / 100) * (60 / 100) * summary['Total_Credit']
    summary['Earnings'] = (
        summary['Total_Repayment'] +
        summary['Profit_on_Credit'] -
        summary['Total_Credit'] -
        summary['Interest_Cost']
    )
    summary['Status'] = summary['Earnings'].apply(lambda x: '✅ Profit' if x >= 0 else '❌ Loss')

    print(f"\n💳 CREDIT ANALYSIS (Margin={margin_pct}%, Interest={interest_rate}%/month)")
    print(summary[['Customer_Name','Total_Credit','Total_Repayment',
                   'Interest_Cost','Earnings','Status']].to_string(index=False))
    print(f"\n   Total Earnings from all credit customers: ₹{summary['Earnings'].sum():,.2f}")
    return summary


def kishore_activity(credit_df):
    """Analyse Kishore's problematic repayment pattern."""
    k = credit_df[
        (credit_df['Customer_Name'] == 'Kishore') &
        (credit_df['Transaction_Date'] != '2024-01-15')
    ].copy()
    k['Transaction_Date'] = pd.to_datetime(k['Transaction_Date'])
    k = k.sort_values('Transaction_Date')

    print("\n⚠️  KISHORE CREDIT ACTIVITY (Feb 6–14 issue)")
    feb_issue = k[(k['Transaction_Date'] >= '2024-02-06') & (k['Transaction_Date'] <= '2024-02-14')]
    print(feb_issue[['Transaction_Date','Credit_Amount','Repayment','Outstanding_Balance']].to_string(index=False))
    return k


# ─────────────────────────────────────────────────────────────────
# VISUALIZATIONS
# ─────────────────────────────────────────────────────────────────

def plot_profit_trend(daily_df):
    """Plot daily profit over time."""
    fig, ax = plt.subplots(figsize=(12, 4))
    df = daily_df.copy()
    ax.plot(df['Date'], df['Profit'], color='#2563eb', linewidth=1.8, marker='o', markersize=3)
    ax.axhline(y=daily_df[daily_df['Business_Open']=='Yes']['Profit'].mean(),
               color='orange', linestyle='--', linewidth=1, label='Mean Profit')
    ax.fill_between(df['Date'], df['Profit'], alpha=0.08, color='#2563eb')
    ax.set_title('Daily Profit Trend — Raj Kishore Gupta & Sons\nMubarakpur, Azamgarh', fontsize=13, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Profit (₹)')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('../dashboards/profit_trend.png', dpi=150)
    plt.show()
    print("Saved: dashboards/profit_trend.png")


def plot_margin_regression(daily_df):
    """Scatter plot with regression line — % Margin vs Profit."""
    df = daily_df[(daily_df['Profit'] != 0) & (daily_df['Pct_Margin'] != 0)]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.regplot(x='Pct_Margin', y='Profit', data=df, ax=ax,
                scatter_kws={'color':'#2563eb', 'alpha':0.7},
                line_kws={'color':'#f97316', 'linewidth':2})
    ax.set_title('Profit vs % Margin — Linear Regression', fontsize=13, fontweight='bold')
    ax.set_xlabel('% Margin')
    ax.set_ylabel('Daily Profit (₹)')
    ax.axvline(x=35, color='green', linestyle='--', linewidth=1, label='Target 35%')
    ax.legend()
    plt.tight_layout()
    plt.savefig('../dashboards/margin_regression.png', dpi=150)
    plt.show()
    print("Saved: dashboards/margin_regression.png")


def plot_credit_earnings(credit_summary_df):
    """Bar chart of earnings per credit customer."""
    fig, ax = plt.subplots(figsize=(9, 4))
    colors = ['#16a34a' if e >= 0 else '#dc2626' for e in credit_summary_df['Earnings']]
    ax.bar(credit_summary_df['Customer_Name'], credit_summary_df['Earnings'], color=colors, edgecolor='white')
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.set_title('Earnings per Credit Customer (at 35% Margin, 4% Interest)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Customer')
    ax.set_ylabel('Earnings (₹)')
    for i, (_, row) in enumerate(credit_summary_df.iterrows()):
        ax.text(i, row['Earnings'] + 100, f"₹{row['Earnings']:,.0f}", ha='center', fontsize=9)
    plt.tight_layout()
    plt.savefig('../dashboards/credit_earnings.png', dpi=150)
    plt.show()
    print("Saved: dashboards/credit_earnings.png")


def plot_vegetable_margins(ideal_margins):
    """Horizontal bar chart of ideal margins per vegetable."""
    fig, ax = plt.subplots(figsize=(9, 6))
    colors = ['#1d4ed8' if m >= 15 else '#60a5fa' for m in ideal_margins.values]
    ax.barh(ideal_margins.index, ideal_margins.values, color=colors, edgecolor='white')
    ax.set_title('Ideal Margin per Vegetable (₹/kg)\nFiltered Days: 34–36% Overall Margin', fontsize=12, fontweight='bold')
    ax.set_xlabel('Margin (₹/kg)')
    for i, v in enumerate(ideal_margins.values):
        ax.text(v + 0.2, i, f'₹{v}', va='center', fontsize=9)
    plt.tight_layout()
    plt.savefig('../dashboards/vegetable_margins.png', dpi=150)
    plt.show()
    print("Saved: dashboards/vegetable_margins.png")


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("\n🚀 Running BDM Project Analysis...")
    print("   Student : Namra Sania | Roll No: 23f2000313")
    print("   Business: Raj Kishore Gupta & Sons, Mubarakpur, Azamgarh\n")

    veg_df, daily_df, credit_df = load_data()

    # 1. Financial Overview
    open_days = financial_overview(daily_df)

    # 2. Margin Analysis
    model, slope, intercept, corr = margin_regression(daily_df)
    variety_profit_correlation(daily_df)
    ideal = ideal_margins_per_vegetable(veg_df, daily_df)

    # 3. Credit Analysis
    cs = credit_summary(credit_df)
    kishore_activity(credit_df)

    # 4. Plots
    plot_profit_trend(daily_df)
    plot_margin_regression(daily_df)
    plot_credit_earnings(cs)
    plot_vegetable_margins(ideal)

    print("\n✅ Analysis complete!")
