import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('wallet.db')
cursor = conn.cursor()

# Create User Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    thai_id TEXT UNIQUE NOT NULL,
    phone_number TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE,
    address TEXT
);
""")

# Create Account Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS account (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    balance REAL DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
""")

# Create Transaction Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    transaction_type TEXT CHECK(transaction_type IN ('top_up', 'transfer', 'pay', 'scan')) NOT NULL,
    destination_acc INTEGER,
    amount REAL NOT NULL,
    description TEXT,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    latitude REAL,
    longitude REAL,
    time TIME,
    FOREIGN KEY (account_id) REFERENCES account(account_id),
    FOREIGN KEY (destination_acc) REFERENCES account(account_id)
);
""")

# Commit changes and close connection
conn.commit()
conn.close()
