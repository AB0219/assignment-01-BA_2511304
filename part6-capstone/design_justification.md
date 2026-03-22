## Storage Systems

The system uses a combination of multiple storage technologies to support different requirements. For transactional operations such as patient records, billing, and day-to-day hospital activities, a relational database like MySQL or PostgreSQL is used. This ensures ACID compliance, which is critical for maintaining accurate and consistent medical data.

For handling large volumes of raw and diverse data such as ICU vitals, doctor notes, and logs, a Data Lake (e.g., Amazon S3 or Hadoop) is used. This allows storage of structured, semi-structured, and unstructured data at scale without requiring a predefined schema.

A Data Warehouse (such as Snowflake or BigQuery) is used for reporting and analytics. Cleaned and transformed data from the data lake is loaded into the warehouse, enabling efficient querying for monthly reports like bed occupancy and department-wise costs.

Additionally, a Vector Database (such as FAISS or Pinecone) is used to store embeddings of clinical notes and patient history. This enables semantic search functionality, allowing doctors to query patient data in natural language and retrieve contextually relevant results.

## OLTP vs OLAP Boundary

The OLTP system consists of the relational database that handles real-time transactional operations such as updating patient records, recording treatments, and managing billing. This layer prioritizes consistency, low latency, and reliability.

The OLAP system begins at the data warehouse, where data is aggregated and optimized for analytical queries. Data flows from the OLTP system into the data lake through ETL processes, and then into the warehouse after cleaning and transformation. The OLAP layer supports reporting, dashboards, and machine learning workflows.

Thus, the boundary lies between the transactional database and the data lake/warehouse pipeline, where data transitions from operational use to analytical use.

## Trade-offs

One significant trade-off in this design is the increased system complexity due to the use of multiple storage systems. Managing a relational database, data lake, data warehouse, and vector database requires additional infrastructure, integration effort, and maintenance.

However, this trade-off is necessary to meet the diverse requirements of the system, including real-time processing, large-scale storage, analytics, and semantic search. To mitigate this complexity, the system can use managed cloud services such as AWS, Google Cloud, or Azure, which simplify deployment and scaling.

Additionally, proper data pipelines and orchestration tools like Apache Airflow can be used to automate data movement and ensure reliability. Monitoring and logging systems can also help detect issues early.

Despite the added complexity, this architecture provides flexibility, scalability, and performance, making it suitable for a modern AI-powered healthcare system.
