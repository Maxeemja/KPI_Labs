import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
sns.set(font_scale=1.2)


def load_data(file_path):
    xls = pd.ExcelFile(file_path)
    print(f"Листи у файлі: {xls.sheet_names}")
    sales_data = pd.read_excel(file_path, sheet_name="Sales Data")
    sale_data = pd.read_excel(file_path, sheet_name="SaleData")
    return sales_data, sale_data


def explore_data(df, sheet_name):
    print(f"\n=== Огляд даних з листа '{sheet_name}' ===")
    print(f"Розмір даних: {df.shape}")
    print("\nПерші 5 рядків:")
    print(df.head())
    print("\nТипи даних:")
    print(df.dtypes)
    print("\nСтатистичний огляд:")
    print(df.describe())
    print("\nПеревірка пропущених значень:")
    print(df.isnull().sum())
    df_cleaned = df.dropna(subset=df.columns[:-3], how='all')
    return df_cleaned


def clean_data(df):
    print("Кількість пропущених значень до очищення:")
    print(df.isnull().sum())
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())
    categorical_cols = df.select_dtypes(exclude=['number']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    print("\nКількість пропущених значень після очищення:")
    print(df.isnull().sum())
    return df


def analyze_sales_by_region(df):
    region_sales = df.groupby('Region')['Sale_amt'].sum().sort_values(ascending=False)
    region_count = df.groupby('Region').size()
    avg_transaction = df.groupby('Region')['Sale_amt'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=region_sales.index, y=region_sales.values)
    plt.title('Загальна сума продажів за регіонами')
    plt.xlabel('Регіон')
    plt.ylabel('Сума продажів')
    plt.tight_layout()
    return region_sales, region_count, avg_transaction


def analyze_sales_by_item(df):
    item_sales = df.groupby('Item')['Sale_amt'].sum().sort_values(ascending=False)
    item_units = df.groupby('Item')['Units'].sum().sort_values(ascending=False)
    item_avg_price = df.groupby('Item')['Unit_price'].mean()
    return item_sales, item_units, item_avg_price


def analyze_sales_by_personnel(df):
    manager_sales = df.groupby('Manager')['Sale_amt'].sum().sort_values(ascending=False)
    salesman_sales = df.groupby('SalesMan')['Sale_amt'].sum().sort_values(ascending=False)
    combined_sales = df.groupby(['Manager', 'SalesMan'])['Sale_amt'].sum().sort_values(ascending=False)
    return manager_sales, salesman_sales, combined_sales


def time_series_analysis(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df['Year'] = df['OrderDate'].dt.year
    df['Month'] = df['OrderDate'].dt.month
    df['Quarter'] = df['OrderDate'].dt.quarter
    monthly_sales = df.groupby(['Year', 'Month'])['Sale_amt'].sum().reset_index()
    quarterly_sales = df.groupby(['Year', 'Quarter'])['Sale_amt'].sum().reset_index()
    plt.figure(figsize=(14, 8))
    for year in df['Year'].unique():
        year_data = monthly_sales[monthly_sales['Year'] == year]
        plt.plot(year_data['Month'], year_data['Sale_amt'], marker='o', linewidth=2, label=f'Рік {year}')
    plt.title('Щомісячні продажі по роках')
    plt.xticks(range(1, 13))
    plt.legend()
    plt.tight_layout()
    return monthly_sales, quarterly_sales


def comprehensive_analysis(df):
    region_top_items = {}
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        top_items = region_data.groupby('Item')['Sale_amt'].sum().sort_values(ascending=False).head(3)
        region_top_items[region] = top_items
    item_quarterly_sales = df.groupby(['Item', 'Quarter'])['Sale_amt'].mean().unstack()
    region_top_salesmen = {}
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        top_salesmen = region_data.groupby('SalesMan')['Sale_amt'].sum().sort_values(ascending=False).head(3)
        region_top_salesmen[region] = top_salesmen
    item_monthly_sales = df.pivot_table(index='Item', columns='Month', values='Sale_amt', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(14, 10))
    sns.heatmap(item_monthly_sales, cmap='YlGnBu', annot=True, fmt='.0f')
    plt.title('Теплова карта продажів за місяцями та товарами')
    plt.tight_layout()
    return item_quarterly_sales, region_top_items, region_top_salesmen


def sales_dynamics(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    df['Month_Year'] = df['OrderDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month_Year')['Sale_amt'].sum()
    plt.figure(figsize=(14, 6))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Динаміка продажів за місяцями')
    plt.xlabel('Місяць')
    plt.ylabel('Сума продажів')
    plt.grid(True)
    plt.tight_layout()
    return monthly_sales


def print_conclusions(region_sales, manager_sales, salesman_sales, item_sales, df):
    print("\n=== Ключові висновки ===")
    print(f"1. Найприбутковіший регіон: {region_sales.index[0]} ({region_sales.iloc[0]:.2f})")
    print(f"2. Найкращий менеджер: {manager_sales.index[0]} ({manager_sales.iloc[0]:.2f})")
    print(f"3. Найкращий продавець: {salesman_sales.index[0]} ({salesman_sales.iloc[0]:.2f})")
    print(f"4. Найбільш прибутковий товар: {item_sales.index[0]} ({item_sales.iloc[0]:.2f})")
    if 'Year' in df.columns and df['Year'].nunique() > 1:
        years = sorted(df['Year'].unique())
        sales_by_year = df.groupby('Year')['Sale_amt'].sum()
        change = ((sales_by_year[years[-1]] - sales_by_year[years[0]]) / sales_by_year[years[0]]) * 100
        direction = "зросли" if change > 0 else "знизились"
        print(f"5. Продажі {direction} на {abs(change):.2f}% з {years[0]} по {years[-1]}")


def main(file_path):
    sales_data, sale_data = load_data(file_path)
    df = explore_data(sales_data, "Sales Data")
    df = clean_data(df)
    region_sales, region_count, avg_transaction = analyze_sales_by_region(df)
    item_sales, item_units, item_avg_price = analyze_sales_by_item(df)
    manager_sales, salesman_sales, combined_sales = analyze_sales_by_personnel(df)
    monthly_sales, quarterly_sales = time_series_analysis(df)
    item_quarterly_sales, region_top_items, region_top_salesmen = comprehensive_analysis(df)
    sales_trend = sales_dynamics(df)
    print_conclusions(region_sales, manager_sales, salesman_sales, item_sales, df)
    plt.show()


if __name__ == "__main__":
    file_path = "Data_Set_5.xlsx"  
    main(file_path)
