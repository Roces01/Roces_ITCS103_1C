from openpyxl import Workbook
from datetime import datetime

workbook = Workbook()
sheet = workbook.active
sheet.title = "Favorite People"

headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
sheet.append(headers)


current_year = datetime.now().year


records = []

for i in range(1, 4):
    print(f"\nEnter information for Favorite Person #{i}")
    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_year = int(input("Birth Year: "))

    
    age = current_year - birth_year

    
    person_id = i


    record = [person_id, first_name, last_name, birth_year, age]
    records.append(record)

    
    sheet.append(record)


file_name = "favorite_people.xlsx"
workbook.save(file_name)

print(f"\nData successfully saved to '{file_name}'")


print("\nSaved Records:")
print("-" * 50)

for record in records:
    print(f"ID: {record[0]}")
    print(f"First Name: {record[1]}")
    print(f"Last Name: {record[2]}")
    print(f"Birth Year: {record[3]}")
    print(f"Age: {record[4]}")
    print("-" * 50)
