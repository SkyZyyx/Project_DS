# Phase 3 Explained - What Each Column Does

## 📊 New Columns We Added:

### 1. **Month** Column
```python
df['Month'] = df['Date'].dt.strftime('%B')
```
**What it does:** Extracts the month name from the date  
**Example:** `2025-01-01` → `"January"`  
**Why?** Easier to read than dates, better for reports

---

### 2. **Total_Sales** Column
```python
df['Total_Sales'] = df['Product_A'] + df['Product_B'] + df['Product_C'] + df['Product_D']
```
**What it does:** Sums all 4 products for each month  
**Example:** If January had A=74, B=74, C=34, D=43 → Total=225  
**Why?** Shows overall monthly performance

---

### 3. **Average_Sales** Column
```python
df['Average_Sales'] = (df['Product_A'] + ... + df['Product_D']) / 4
```
**What it does:** Calculates average sales across products  
**Example:** Total=225 / 4 products = 56.25  
**Why?** Shows typical product performance per month

---

### 4. **Month_over_Month_Growth** Column ⭐ (Most Important!)
```python
df['Month_over_Month_Growth'] = df['Total_Sales'].pct_change() * 100
```
**What it does:** Shows % change from previous month  
**Example:** 
- January: 225 (no previous month, shows NaN)
- February: 143 → **-36.4%** (big drop!)
- March: 226 → **+58.0%** (huge recovery!)

**Why?** Identifies growth trends and problem months

---

### 5. **Quarter** Column
```python
month_num = df['Date'].dt.month
df['Quarter'] = 'Q' + ((month_num - 1) // 3 + 1).astype(str)
```
**What it does:** Groups months into business quarters  
**Logic:**
- Months 1-3 (Jan-Mar) → Q1
- Months 4-6 (Apr-Jun) → Q2
- Months 7-9 (Jul-Sep) → Q3
- Months 10-12 (Oct-Dec) → Q4

**Why?** Businesses report quarterly results

---

### 6. **Max_Sales_Product** Column
```python
df['Max_Sales_Product'] = df[product_cols].idxmax(axis=1)
```
**What it does:** Finds which product sold most each month  
**Example:** In January, Product_A and Product_B both had 74 units → "Product_A" (first one wins)  
**Why?** Identifies star performers

---

### 7. **Min_Sales_Product** Column
```python
df['Min_Sales_Product'] = df[product_cols].idxmin(axis=1)
```
**What it does:** Finds which product sold least each month  
**Example:** In January, Product_C had 34 units (lowest) → "Product_C"  
**Why?** Identifies products needing attention

---

## 🔍 Real Insights from Your Data:

Looking at the Final.csv output:

### Best/Worst Months:
- **Worst:** February (143 sales, -36.4% drop) ⚠️
- **Best:** December (237 sales) 🎉

### Growth Patterns:
- Biggest drop: February (-36.4%)
- Biggest gain: March (+58.0%)
- Most months had positive growth after February

### Product Performance:
- **Product_A** dominated! It was the Max seller in 11/12 months
- **Product_D** struggled - it was the Min seller in 10/12 months
- **Product_B** only won once (April with 80 units)

### Quarterly Preview (we'll analyze deeper in Phase 4):
- Q1: 225 + 143 + 226 = 594
- Q2: 211 + 209 + 166 = 586
- Q3: 162 + 182 + 232 = 576
- Q4: 198 + 228 + 237 = 663 (best quarter!)

---

## 💡 Key Pandas Concepts You Just Learned:

1. **`.pct_change()`** - Calculate percentage change between rows
2. **`dt.month`** - Extract parts from datetime columns
3. **`.idxmax(axis=1)`** - Find column name with max value per row
4. **Integer division `//`** - Used for quarter calculation

---

## ✅ What You Have Now:

**File:** `data/Final.csv`  
**Columns:** 12 total (5 original + 7 new)  
**Rows:** 12 (one per month)

This enhanced dataset is now ready for:
- Pivot table analysis (Phase 4)
- Extracting key insights (Phase 5)
- Creating visualizations (Phase 6)
