"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"{name} is already in contacts.")
        else:
            self.contacts[name] = phone
            print(f"Contact added: {name} → {phone}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"{name} not found in contacts.")

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found.")

    def show_contacts(self):
        if not self.contacts:
            return "No contacts available."
        return self.contacts
book = ContactBook()
book.add_contact("Alice", "08012345678")
book.add_contact("Tom", "09020202020")
print(book.search_contact("Alice"))  