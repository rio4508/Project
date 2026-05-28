class Contact:

    phone_directory = []

    def __init__(self,name,phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)


    def show_contact(self):
        return f"name: {self.name}, phone: {self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("no contact found")
        else:
            print("All the contact in the directory=>")
            for contact in cls.phone_directory:
                print(contact.show_contact())


    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
               return contact.phone

        return f"NO contact found {search_name}"
    @staticmethod
    def valid(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
n_contact = int(input("How many number you want to add?"))
for i in range(n_contact):
   name =(input("Please enter the name: "))
   phone_number = (input("Please enter the phone number: "))
   if Contact.valid(phone_number):
       Contact(name,phone_number)
   else:
       print("Invalid phone number")



Contact.show_all_contact()
