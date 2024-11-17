import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('wallet.db')
cursor = conn.cursor()

# SQL query to calculate sums
query = """
SELECT 
    SUM(CASE WHEN transaction_type = 'top_up' THEN amount ELSE 0 END) AS total_top_up,
    SUM(CASE WHEN transaction_type IN ('transfer', 'pay', 'scan') THEN amount ELSE 0 END) AS total_others
FROM transactions;
"""

# Execute the query
cursor.execute(query)

# Fetch the results
result = cursor.fetchone()
total_top_up = result[0]  # Sum of top_up amounts
total_others = result[1]  # Sum of transfer, pay, and scan amounts

# Print the results
print(f"Total Top-Up: {total_top_up}")
print(f"Total (Transfer, Pay, Scan): {total_others}")

# Close connection
conn.close()