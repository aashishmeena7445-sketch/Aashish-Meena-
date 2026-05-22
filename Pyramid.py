def pyramid(rows):
    for i in range(1, rows + 1):
        # Prints spaces, then prints stars
        print(" " * (rows - i) + "*" * (2 * i - 1))

# --- How to use it ---
pyramid(5)

