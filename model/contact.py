class Contact():
    def __init__(self,id:int=None, name:str=None, telephone:str=None, email:str=None, favorite:bool=False):
        self.id = id
        self.name = name
        self.telephone = telephone
        self.email = email
        self.favorite = favorite

    def textoFavorito(self):
        return "Sim" if self.favorite else "Não"
    
    def __str__(self):
        return f"Nome: {self.name}\nTelefone: {self.telephone}\nEmail: {self.email}\nFavorito: {self.textoFavorito()}"
    
    def __repr__(self):
        return (
            f"Contact(id='{self.id}'name='{self.name}', telephone='{self.telephone}', "
            f"email='{self.email}', favorite={self.favorite})"
        )
    
    def __eq__(self, object:object):
        if not isinstance(object,Contact):
            return False
        return self.id == object.id
    
    def __hash__(self):
        return hash(self.id)