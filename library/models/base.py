from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class ListTypes(str, Enum):
    unordered = 'unordered'
    ordered = 'ordered'
    scroll = 'scroll'


class Name(BaseModel):
    name: str
    subname: str | None = None


class DateRange(BaseModel):
    start: str | datetime
    end: str | datetime | None = None


class Link(BaseModel):
    text: str
    ref: str


class RawText(BaseModel):
    text: str
    includes: list[Link] = []


class MarkedRawText(RawText):
    mark: int


class RawTextList(BaseModel):
    type: ListTypes = ListTypes.unordered
    title: str | None = None
    items: list[MarkedRawText] | list[str | RawText | RawTextList]
