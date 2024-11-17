import sqlite3
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect('wallet.db')
cursor = conn.cursor()

# Mock data to insert
mock_data = [
    (1, 'top_up', None, 600.0, '2024-11-17 19:00:00', None, None, '19:00:00'),
    (1, 'transfer', 2, 250.0, '2024-11-17 19:05:00', None, None, '19:05:00'),
    (1, 'pay', 2, 180.0, '2024-11-17 19:10:00', None, None, '19:10:00'),
    (1, 'scan', 2, 160.0, '2024-11-17 19:15:00', None, None, '19:15:00'),
    (1, 'top_up', None, 700.0, '2024-11-17 20:00:00', None, None, '20:00:00'),
    (1, 'pay', 2, 140.0, '2024-11-17 20:05:00', None, None, '20:05:00'),
    (1, 'scan', 2, 170.0, '2024-11-17 20:10:00', None, None, '20:10:00'),
    (1, 'transfer', 2, 280.0, '2024-11-17 20:15:00', None, None, '20:15:00'),
    (1, 'top_up', None, 800.0, '2024-11-17 21:00:00', None, None, '21:00:00'),
    (1, 'scan', 2, 130.0, '2024-11-17 21:05:00', None, None, '21:05:00'),
    (1, 'pay', 2, 150.0, '2024-11-17 21:10:00', None, None, '21:10:00'),
    (1, 'transfer', 2, 310.0, '2024-11-17 21:15:00', None, None, '21:15:00'),
    (1, 'top_up', None, 900.0, '2024-11-17 22:00:00', None, None, '22:00:00'),
    (1, 'pay', 2, 120.0, '2024-11-17 22:05:00', None, None, '22:05:00'),
    (1, 'scan', 2, 140.0, '2024-11-17 22:10:00', None, None, '22:10:00'),
    (1, 'transfer', 2, 270.0, '2024-11-17 22:15:00', None, None, '22:15:00'),
    (1, 'top_up', None, 1000.0, '2024-11-17 23:00:00', None, None, '23:00:00'),
    (1, 'scan', 2, 200.0, '2024-11-17 23:05:00', None, None, '23:05:00'),
    (1, 'pay', 2, 180.0, '2024-11-17 23:10:00', None, None, '23:10:00'),
    (1, 'transfer', 2, 350.0, '2024-11-17 23:15:00', None, None, '23:15:00'),
]

# Insert mock data into the transaction table
for data in mock_data:
    cursor.execute("""
        INSERT INTO transactions (account_id, transaction_type, destination_acc, amount, transaction_date, latitude, longitude, time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

# Commit changes and close connection
conn.commit()
conn.close()
