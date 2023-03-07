from pydantic import BaseModel

from base import Link, Paragraph


class Contact(BaseModel):
    type: str
    content: Link | str


class ShortInfo(BaseModel):
    photo: str
    name: str
    position: str
    parts: list[Paragraph]
    contacts: list[Contact]
