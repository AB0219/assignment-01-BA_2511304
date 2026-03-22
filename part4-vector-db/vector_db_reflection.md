## Vector DB Use Case

A traditional keyword-based database search would not be sufficient for searching large legal contracts using natural language queries. Keyword search relies on exact word matches, which means it may fail if the wording in the contract differs from the user's query. For example, a lawyer searching for "termination clauses" might miss relevant sections labeled as "contract cancellation terms" or "agreement exit conditions."

This limitation makes keyword search ineffective for understanding the semantic meaning of text. Legal documents often use complex and varied language, making it difficult to retrieve accurate results using simple text matching.

A vector database addresses this problem by using embeddings to capture the semantic meaning of text. Each section of the contract can be converted into a vector representation using models like sentence-transformers. Similarly, the user's query is converted into a vector. The system then performs similarity search to find the most relevant sections based on meaning rather than exact wording.

This allows the system to return accurate and contextually relevant results even when the query and the document use different phrasing. Vector databases are also optimized for fast similarity search, making them suitable for large-scale documents like 500-page contracts.

Therefore, a vector database plays a crucial role in enabling intelligent, semantic search capabilities that go beyond traditional keyword-based approaches.
