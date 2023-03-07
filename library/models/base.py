from datetime import datetime

from pydantic import BaseModel


class DateRange(BaseModel):
    start: str | datetime
    end: str | datetime


class Link(BaseModel):
    ref: str
    name: str


class Paragraph(BaseModel):
    text: str
    links: list[Link]


class Skill(BaseModel):
    skill: str


class SkillWithMark(Skill):
    mark: int


class SkillsPack(BaseModel):
    name: str
    skills: Skill


class SkillsPackWithMarks(SkillsPack):
    skills: SkillWithMark
