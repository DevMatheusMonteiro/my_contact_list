from mock.contacts import contacts
from model.contact import Contact
from dto.contact_dto_input import ContactDTOInput

class ContactRepository():
    @staticmethod
    def create(created_contact:ContactDTOInput):
        contact = Contact()
        for key, value in created_contact.model_dump(exclude_unset=True).items():
            setattr(contact, key, value)
        contacts.append(contact)
        return contact
    
    @staticmethod
    def index():
        return contacts
    
    @staticmethod
    def show(id:int):
        return next((contact for contact in contacts if contact.id == id), None)
    
    @staticmethod
    def update(id, updated_contact: ContactDTOInput):
        contact = ContactRepository.show(id)
        for key, value in updated_contact.model_dump(exclude_unset=True).items():
            setattr(contact, key, value)
        return contact
    
    @staticmethod
    def delete(removed_contact:Contact):
        contacts.remove(removed_contact)
        return removed_contact