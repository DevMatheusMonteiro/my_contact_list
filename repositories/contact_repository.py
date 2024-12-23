from mock.contacts import contacts
from model.contact import Contact

class ContactRepository():
    @staticmethod
    def create(created_contact:Contact):
        contacts.append(created_contact)
        return created_contact
    
    @staticmethod
    def index():
        return contacts
    
    @staticmethod
    def show(id):
        return next((contact for contact in contacts if contact.id == id), None)
    
    @staticmethod
    def update(id, updated_contact:Contact):
        contact = ContactRepository.show(id)
        contact = updated_contact
        return contact
    
    @staticmethod
    def delete(removed_contact:Contact):
        contacts.remove(removed_contact)
        return removed_contact

