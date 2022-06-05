# -*- coding: utf-8 -*-

#Programming Lab 1 Lesson

import json

class ContactInfo:
    
    def __init__(self, name, surname, email, phone_number):

        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
    
    def print_contacts_details(self):
        
        print(f"Hello, this is the list of your {self.contacts_name}")
        
            
class Agenda:
    
    def __init__(self):
        
        self.contact_list = []

    def length(self):
       
        return len(self.contact_list)
        
    def add_contact(self, contact: ContactInfo):
       
        self.contact_list.append(contact)
        
    def delete_contact(self, index):
    
        del self.contact_list[index]
           
            
    def show_agenda(self):
      
        number_of_contacts = self.length()
        if number_of_contacts == 0:
            print("Sorry the agenda is empty")
            
        else:
            for contact in self.contact_list:
                index = self.contact_list.index(contact)
                print(f"{index} - {contact.name} {contact.surname} {contact.email} {contact.phone_number}")
    
            
    def search_by_name(self, name):
        for contact in self.contact_list:
            if name in contact.name:
                print(f"{contact.name} {contact.surname} {contact.email} {contact.phone_number}")

    def search_by_surname(self, surname):
        for contact in self.contact_list:
            if surname in contact.surname:
                print(f"{contact.name} {contact.surname} {contact.email} {contact.phone_number}")
                
    def search_by_email(self, email):
        for contact in self.contact_list:
            if email in contact.email:
                print(f"{contact.name} {contact.surname} {contact.email} {contact.phone_number}")
    
    def search_by_phone(self, phone_number):
        for contact in self.contact_list:
            if phone_number in contact.phone_number:
                print(f"{contact.name} {contact.surname} {contact.email} {contact.phone_number}")
                
                
    def search(self, keyword):
        
        for contact in self.contact_list:
            index = self.contact_list.index(contact)
            if keyword in contact.name or keyword in contact.surname or keyword in contact.email or keyword in contact.phone_number:
                print(f"{index} - {contact.name} {contact.surname} {contact.email} {contact.phone_number}")
                
    def store_agenda(self, filename): 

        with open(filename, "w") as f:
            dict_list = []       
            for contact in self.contact_list:
                dict_list.append(contact.__dict__)
            json.dump(dict_list, f)
            
    def restore_agenda(self, filename):
        filenme = 'agenda.json'
        with open(filename) as f:
            dict_list = json.load(f)
        print(dict_list)
    
my_agenda = Agenda()

input_user = -1

while input_user != 0:
    
    print("\nTo adding a contact press 1")
    print("To search contacts press 2")
    print("To delete a contact press 3")
    print("To show all contacts press 4")
    print("To search contact by phone press 5")
    print("To exit press 0")
    input_user = int(input("Press a number: "))
    
    if input_user == 1:
        
        new_contact_name = input("Whats the Name of the new contact that you want add?: ")
        new_contact_surname = input("Whats the Surname of the new contact that you want add?: ")
        new_contact_phone = input("Insert the phone of the contact: ")
        new_contact_email = input("Insert the email of the contact: ")
        
        my_contact = ContactInfo(new_contact_name, new_contact_surname, new_contact_email, new_contact_phone)
        my_agenda.add_contact(my_contact)
        print("The contact is added!\n")

    if input_user == 2:
        
        search_keyword = input("Search contact: ")
        my_agenda.search(search_keyword)
        
    if input_user == 3:
        
        my_agenda.show_agenda()

        agenda_length = my_agenda.length()
        
        if agenda_length > 0: 
            index_to_delete = input("Insert the contact index to delete: ")
            my_agenda.delete_contact(int(index_to_delete))
            print("The contact is deleted!\n")
        else:
            print("Agenda is empty!\n")

    if input_user == 4:
        
        my_agenda.show_agenda()
     
    if input_user == 5:
        
        search_keyword = input("Search contact by phone: ")
        my_agenda.search_by_phone(search_keyword)
        
        
my_agenda.store_agenda("agenda.json")
my_agenda.restore_agenda("agenda.json")




        
    
    
    