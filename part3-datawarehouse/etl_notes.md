## ETL Decisions

### Decision 1 — Standardizing Date Formats
Problem: The raw dataset contained inconsistent date formats such as DD-MM-YYYY and MM/DD/YYYY, making it difficult to perform time-based analysis.
Resolution: All dates were converted into a standard ISO format (YYYY-MM-DD) before loading into the dim_date table. This ensures consistency and enables proper sorting and aggregation.

### Decision 2 — Handling NULL Values
Problem: Some records had missing values in important fields such as product category and total amount.
Resolution: NULL values were either replaced with default values (e.g., 'Unknown' for category) or excluded if critical. This ensured that analytical queries would not produce incorrect or misleading results.

### Decision 3 — Standardizing Category Names
Problem: Product categories appeared in different formats such as 'electronics', 'ELECTRONICS', and 'Electronics'.
Resolution: All category values were standardized to a consistent format (e.g., 'Electronics', 'Clothing', 'Groceries') before inserting into the dim_product table. This avoids duplication and ensures accurate grouping in reports.
