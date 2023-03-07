from pydantic import BaseModel

from base import DateRange, Paragraph, SkillsPack, SkillsPackWithMarks


class AboutMe(BaseModel):
    parts: list[Paragraph]


class Education(BaseModel):
    date_range: DateRange
    direction: str
    name: str
    parts: list[Paragraph]


class Job(BaseModel):
    date_range: DateRange
    direction: str
    name: str
    parts: list[Paragraph]
    skills_pack: list[SkillsPack]


class HardSkills(BaseModel):
    skills: list[SkillsPackWithMarks]
    parts: list[Paragraph]


class Sections(BaseModel):
    about_me: AboutMe
    education: list[Education]
    experience: list[Job]
    hard_skills: HardSkills
