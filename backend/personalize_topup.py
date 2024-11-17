import sqlite3

def calculate_personalize_top_up():
    # Connect to SQLite database
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()

    # Step 1: Get the last 10 top-up amounts
    query = """
    SELECT amount, transaction_date 
    FROM transactions
    WHERE transaction_type = 'top_up'
    ORDER BY transaction_date DESC
    LIMIT 10;
    """
    cursor.execute(query)
    top_up_history = [row[0] for row in cursor.fetchall()]
    print(top_up_history)

    avg_top_up = sum(top_up_history) / len(top_up_history)
    threshold = 4 * avg_top_up

    # Step 2: Retrieve transactions (transfer, pay, scan) until their cumulative sum is closest to the threshold
    cursor.execute("""
        SELECT amount
        FROM transactions
        WHERE transaction_type IN ('transfer', 'pay', 'scan')
        ORDER BY transaction_date DESC;
    """)
    # transactions = cursor.fetchall()

    # cumulative_sum = 0
    # limited_transactions = []

    # for row in transactions:
    #     amount = row[0]
    #     if cumulative_sum + amount < threshold:
    #         cumulative_sum += amount
    #         limited_transactions.append(amount)
    #     else:
    #         break
    expense_transactions = [row[0] for row in cursor.fetchall()]

    # Step 3: Find multiple closest sums using get_closest_sum function
    closest_sums = []
    start_index = 0

    for _ in range(4):  # Repeat 4 times
        closest_sum, start_index = get_closest_sum(expense_transactions, avg_top_up, start_index)
        closest_sums.append(closest_sum)

        if start_index >= len(expense_transactions):
            break  # Exit if no more transactions to process

    # Close the database connection
    conn.close()

    # Step 4: Calculate the remaining amount and personalized top-up
    total_closest_sum = sum(closest_sums)
    avg_accumulated = total_closest_sum / len(closest_sums)

    return {
        "avg_top_up": avg_top_up,
        "closest_sums": closest_sums,
        "avg_accumulated (personalized top up value)": avg_accumulated
    }


def get_closest_sum(expense_transactions, avg_top_up, start_index):
    """
    Finds the closest sum to avg_top_up from the given transactions starting from start_index.

    Args:
        expense_transactions (list): List of transaction amounts.
        avg_top_up (float): The average top-up amount.
        start_index (int): The index to start searching from.

    Returns:
        tuple: A tuple containing the closest sum and the next starting index.
    """
    closest_sum = 0
    min_diff = float('inf')
    current_sum = 0
    next_index = start_index

    for i in range(start_index, len(expense_transactions)):
        current_sum += expense_transactions[i]
        diff = abs(current_sum - avg_top_up)

        if diff < min_diff:
            min_diff = diff
            closest_sum = current_sum
            next_index = i + 1  # Set next_index to the next transaction

        # Stop adding if current_sum exceeds avg_top_up significantly
        if current_sum > avg_top_up and diff > min_diff:
            break

    return closest_sum, next_index


print(calculate_personalize_top_up())