## Anomaly Analysis
### Insert Anomaly

In the orders_flat.csv table, it is not possible to insert a new product unless there is an associated order.

For example, all product details such as product_id, product_name, and category are tied to an order_id. If a new product (e.g., a new "Laptop") is introduced but has not yet been ordered, there is no way to store its details in the table without creating a dummy order.

This leads to incomplete or forced data entry.
