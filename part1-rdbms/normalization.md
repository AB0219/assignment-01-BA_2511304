## Anomaly Analysis
### Insert Anomaly

In the orders_flat.csv table, it is not possible to insert a new product unless there is an associated order.

Example: all product details such as product_id, product_name, and category are tied to an order_id. If a new product (e.g., a new "Laptop") is introduced but has not yet been ordered, there is no way to store its details in the table without creating a dummy order.

This leads to incomplete or forced data entry.

### Update Anomaly

Customer and product details are repeated across multiple rows.

Example: the same customer_id appears in multiple rows with repeated customer_name and customer_email. If a customer's email changes, it must be updated in all rows where that customer appears.

If one row is missed, the database will contain inconsistent data (old and new email values for the same customer).

This redundancy leads to update anomalies and data inconsistency.

### Delete Anomaly

Deleting a single order row can result in the loss of important information.

Example: if a customer has placed only one order and that order is deleted, all associated customer details (customer_name, email, city) are also lost.

Similarly, product and sales representative information tied only to that order would also be removed.

This leads to unintended data loss.
