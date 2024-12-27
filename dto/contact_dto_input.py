from pydantic import BaseModel
from typing import Optional

class ContactDTOInput(BaseModel):
    name: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
