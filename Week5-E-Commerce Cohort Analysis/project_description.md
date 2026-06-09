# E-COMMERCE CUSTOMER INTELLIGENCE PROJECT

## DATA SOURCE
- **Dataset:** Online Retail II  
- **Source:** Kaggle  

This dataset contains transactional data of a UK-based online retail store.  
It is widely used for customer analytics, cohort analysis, and retail business intelligence.

**Key fields include:**
- Invoice number
- Product description
- Quantity purchased
- Unit price
- Customer ID
- Invoice date
- Country

---

## PROJECT OVERVIEW
This project performs end-to-end data preprocessing, cohort analysis, customer behavior analysis, and business KPI generation using Python (Pandas and NumPy).

The main objective is to extract meaningful business insights such as:
- Customer retention patterns
- Revenue generation trends
- Customer Lifetime Value (LTV)
- High-value customers and products
- Sales performance by time and geography

---

## DATA PREPROCESSING

### 1. Column Cleaning
- Removed leading/trailing spaces from column names
- Standardized column names:

| Original       | Standardized |
|----------------|---------------|
| Invoice        | InvoiceNo     |
| Customer ID    | CustomerID    |
| Price          | UnitPrice     |

### 2. Missing Value Handling
- Removed rows with missing:
  - `InvoiceDate`
  - `CustomerID`

### 3. Date Conversion
InvoiceDate converted to datetime format:  
`pd.to_datetime(InvoiceDate, dayfirst=True, errors='coerce')`

### 4. Data Filtering
- Removed canceled transactions (InvoiceNo starting with 'C')
- Removed invalid transactions:
  - Quantity > 0
  - UnitPrice > 0

---

## FEATURE ENGINEERING

**Revenue Calculation**  
Revenue = Quantity × UnitPrice

**Time-Based Features**  
- InvoiceMonth = Monthly period extracted from InvoiceDate  
- Hour = Hour of transaction

**Cohort Definition**  
CohortMonth = First purchase month per CustomerID

**Cohort Age Calculation**  
InvoiceMonth_int = (Year × 12) + Month  
CohortMonth_int = (Year × 12) + Month  
CohortAge = InvoiceMonth_int − CohortMonth_int

---

## COHORT ANALYSIS

### 1. Retention Calculation
retention = COUNT(DISTINCT CustomerID) grouped by (CohortMonth, CohortAge)

### 2. Retention Matrix
Pivot table:
- index = CohortMonth
- columns = CohortAge
- values = number of active customers

### 3. Retention Rate (%)
retention_rate = (retention_matrix / retention_matrix[0]) × 100

---

## CUSTOMER LIFETIME VALUE (LTV)

**Customer Revenue**  
customer_revenue = SUM(Revenue per CustomerID)

**LTV Values Array**  
ltv_vals = customer_revenue.values

**Key Metrics**  
- Median LTV: median(ltv_vals)  
- VIP Threshold (Top 10% Customers): 90th percentile = np.percentile(ltv_vals, 90)

---

## BUSINESS KEY PERFORMANCE INDICATORS (KPIs)

| KPI | Calculation |
|-----|-------------|
| Total Revenue | SUM(Revenue) |
| Average Order Value (AOV) | MEAN(SUM(Revenue grouped by InvoiceNo)) |
| Peak Sales Hour | ARGMAX(SUM(Revenue grouped by Hour)) |
| Top Country | ARGMAX(SUM(Revenue grouped by Country)) |
| Top Products | Top 10 products by revenue: SUM(Revenue grouped by Description) |
| Top Customers | Top 10 customers by revenue: SUM(Revenue grouped by CustomerID) |

---

## CUSTOMER INSIGHTS

**Pareto Principle (80/20 Rule)**  
- Customers sorted by revenue  
- Cumulative revenue percentage calculated  
- Customers contributing to 80% of revenue identified

**Outlier Detection**  
Revenue outliers defined as:  
Revenue > mean + 3 × standard deviation

---

## OUTPUT FILES GENERATED

1. **cleaned_data.csv** – Final cleaned dataset with engineered features  
2. **retention_matrix.csv** – Cohort retention matrix with customer counts and rates  
3. **business_report.txt** – Summary report containing all KPIs and insights

---

## TECH STACK
- Python
- Pandas
- NumPy

---

**END OF PROJECT DOCUMENT**
