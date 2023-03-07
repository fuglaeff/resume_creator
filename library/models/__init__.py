from pydantic import BaseModel

from left_side_models import ShortInfo
from right_side_models import Sections


__all__ = [
    'ResumeModel'
]


class ResumeModel(BaseModel):
    short_info: ShortInfo
    sections: Sections
