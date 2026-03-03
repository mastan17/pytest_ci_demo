import csv


class Contact:
    def __init__(self, first, last, street, city, state, zip_code, phone, email):
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code   # zip is a string (leading zeros)
        self.phone = phone
        self.email = email

    def print_contact(self):
        print(
            self.last + ", " + self.first + " | " +
            self.street + ", " + self.city + ", " +
            self.state + " " + self.zip_code + " | " +
            self.phone + " | " + self.email
        )


def main():
    contacts = []   # dynamic array (list)

    # open and read csv file
    file = open("us-contacts.csv", "r")
    reader = csv.reader(file)

    for row in reader:
        # skip bad rows
        if len(row) != 8:
            continue

        contact = Contact(
            row[0], row[1], row[2], row[3],
            row[4], row[5], row[6], row[7]
        )

        contacts.append(contact)

    file.close()

    # sort contacts by last name
    contacts.sort(key=lambda c: c.last)

    # print every 50th contact (starting at index 49)
    i = 49
    while i < len(contacts):
        print("Contact #" + str(i + 1))
        contacts[i].print_contact()
        print()
        i += 50


main()