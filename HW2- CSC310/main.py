import csv
from hash_table import HashTable


#Employee object stored as value in hash table
class Employee:
    def __init__(self, employee_id, first, last, email):
        self.employee_id = employee_id
        self.first = first
        self.last = last
        self.email = email

    # string representation for printing
    def __str__(self):
        return self.first + " " + self.last + " (" + self.email + ")"


def main():

    # creat hash table
    table = HashTable()

    # store two keys for testing get/remove
    first_key = None
    second_key = None

    # open CSV file
    with open("us-contacts (2).csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        # uncomment if CSV has a header row
        # header = next(reader)

        # read each row and insert into hash table
        for row in reader:

            if len(row) < 4:
                continue

            employee_id = row[0]
            first = row[1]
            last = row[2]
            email = row[3]

            emp = Employee(employee_id, first, last, email)

            # insert employee into table
            table.insert(employee_id, emp)

            # save first two keys for testing
            if first_key is None:
                first_key = employee_id
            elif second_key is None:
                second_key = employee_id

    # print underlying hash table
    print("Underlying hash table:\n")
    table.print_table()

    #demonstrate get function
    print("\nTesting get:")
    print("Get first key:", first_key, "=>", table.get(first_key))
    print("Get second key:", second_key, "=>", table.get(second_key))

    # demonstrate remove function
    print("\nTesting remove:")
    print("Remove first key:", first_key, "=>", table.remove(first_key))
    print("Get after removal:", first_key, "=>", table.get(first_key))

    print("Remove second key:", second_key, "=>", table.remove(second_key))
    print("Get after removal:", second_key, "=>", table.get(second_key))


# run main program
if __name__ == "__main__":
    main()