from openpyxl import Workbook
from datetime import datetime

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active
sheet.title = "Favorite People"

# Add column headers
headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
sheet.append(headers)

# Get current year
current_year = datetime.now().year

# List to store records
records = []

# Input data for 3 favorite people
for i in range(1, 4):
    print(f"\nEnter information for Favorite Person #{i}")
    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_year = int(input("Birth Year: "))

    # Compute age
    age = current_year - birth_year

    # Assign ID
    person_id = i

    # Store record
    record = [person_id, first_name, last_name, birth_year, age]
    records.append(record)

    # Write to Excel sheet
    sheet.append(record)

# Save the Excel file
file_name = "favorite_people.xlsx"
workbook.save(file_name)

print(f"\nData successfully saved to '{file_name}'")

# Display all saved records
print("\nSaved Records:")
print("-" * 50)

for record in records:
    print(f"ID: {record[0]}")
    print(f"First Name: {record[1]}")
    print(f"Last Name: {record[2]}")
    print(f"Birth Year: {record[3]}")
    print(f"Age: {record[4]}")
    print("-" * 50)
