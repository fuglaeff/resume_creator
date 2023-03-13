from pydantic import BaseModel

from . import base as bs


class Subsection(BaseModel):
    name: bs.Name | str | None = None
    date_range: bs.DateRange | None = None
    elements: list[str | bs.RawText | bs.RawTextList]


class Section(BaseModel):
    name: str | bs.Name
    subsections: list[Subsection] = []


class Resume(BaseModel):
    sections: list[Section]
