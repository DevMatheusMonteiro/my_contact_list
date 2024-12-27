from repositories.contact_repository import ContactRepository
from dto.contact_dto_input import ContactDTOInput
from utils.app_error import AppError

class ContactService():
    @staticmethod
    def create(created_contact: ContactDTOInput):
        created_contact = ContactRepository.create(created_contact)
        return created_contact
    
    @staticmethod
    def index():
        if not ContactRepository.index():
            raise AppError("Lista de contatos vazia.", 404)
        return ContactRepository.index()
    
    @staticmethod
    def show(id:int):
        contact = ContactRepository.show(id)
        if not contact:
            raise AppError("Nenhum contato encontrado", 404)
        return contact
    
    @staticmethod
    def update(id:int, contact_dto_input: ContactDTOInput):
        contact = ContactService.show(id)
        if contact_dto_input.name == "":
            raise AppError("Nome não pode ser vazio")
        if contact_dto_input.email == "":
            raise AppError("Email não pode ser vazio")
        if contact_dto_input.telephone == "":
            raise AppError("Telefone não pode ser vazio")
        updated_contact = ContactRepository.update(contact.id, contact_dto_input)
        return updated_contact

    @staticmethod
    def delete(id:int):
        removed_contact = ContactService.show(id)
        ContactRepository.delete(removed_contact)
        return removed_contact