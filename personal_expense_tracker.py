# Create a program to track expenses and income, saving data to a CSV for future reference.

import csv


def add_expense_funct():
    # New record to add
    new_record = ["12-1-25", "Tuition fees", "Expenses", -250]
    # Open CSV in append mode
    with open("people.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_record)  # Add the new row

    print("New record added successfully!")


def view_expenses_funct():
    # Open the CSV file in read mode
    with open("people.csv", "r") as file:
        reader = csv.reader(file)  # Create a CSV reader object

        # Loop through each row and print it
        for row in reader:
            print(row)


def enter_expenses_funct():

    # Step 1: Read the existing CSV
    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        data2 = list(reader)  # Convert to a list so we can modify it

    # Step 2: Add a new column name to the header
    data2[0].append("Details")  # Add "Details" to the header

    # Step 3: Add a value for each row
    for row in data2[1:]:  # Skip header
        details_input = input("Enter the details for each expense: ")
        row.append(details_input)

    # Step 4: Write everything back to the CSV
    with open("people.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data2)

    print("New column added successfully!")


def es_numero(valor):
    try:
        float(valor)  # Si no se puede convertir, lanza excepción
        return True
    except ValueError:
        return False


def calculate_total_amount_funct():

    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        data2 = list(reader)

    # Skip the header and sum the second column (index 1)
    vector = []
    for row in data2[1:]:
        expense_income = row[3]
        vector.append(expense_income)
    print(f"{vector}")

    if all(es_numero(element) for element in vector):
        numeros = [float(element) for element in vector]
        print(f"La suma es: {sum(numeros)}")
    else:
        print("Hay valores no numéricos en el vector.")

  #  money_balance = sum(int(row[3]) for row in data2[1:])

  #  print(f"Money balance: {money_balance}")


# main
# Sample data
header = ["Date", "Description", "Category", "Amount"]
data = [
    ["1-1-25", "Rent", "Expenses", -300],
    ["5-1-25", "Salary", "Income", 1000],
    ["10-1-25", "Supermarket", "Expenses", -200]
]


# Create and write to a CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)     # Write the header
    writer.writerows(data)      # Write multiple rows

print("CSV file 'people.csv' created successfully!")

add_expense_var = input(
    "Do you want to add a new record to the CVS file?(y=1,n=0): ")
if add_expense_var == "1":
    add_expense_funct()
else:
    pass

view_expenses_var = input(
    "Do you want to display the data from the CVS file?(y=1,n=0): ")
if view_expenses_var == "1":
    view_expenses_funct()
else:
    pass

enter_details_var = input(
    "Do you want to enter details for each expense/income?(y=1,n=0): ")
if enter_details_var == "1":
    enter_expenses_funct()
else:
    pass

calculate_total_amount = input(
    "Do you want to calculate the balance?(y=1,n=0): ")
if calculate_total_amount == "1":
    calculate_total_amount_funct()
else:
    pass
