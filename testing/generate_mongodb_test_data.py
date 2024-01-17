import csv
import random

# List of unique first and last names
first_names = ["John", "Jane", "Robert", "Emily", "Michael", "Sophia", "William", "Olivia", "David", "Emma"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

# Generating 100 rows with unique first and last names and random values
data_with_unique_names = [(f"{random.choice(first_names)} {random.choice(last_names)}", random.randint(1, 1000000)) for _ in range(100)]

# Writing to CSV file
file_path_with_unique_names = "testing/random_data_with_unique_names.csv"  # Replace with your desired file path
with open(file_path_with_unique_names, 'w', newline='') as csvfile:
    fieldnames = ['name', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data_with_unique_names:
        writer.writerow({'name': row[0], 'value': row[1]})

print(f"CSV file with unique names generated successfully at: {file_path_with_unique_names}")