from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional


class Contact(BaseModel):
    facebook: Optional[HttpUrl]
    linkedin: Optional[HttpUrl]
    github: Optional[HttpUrl]
    email: EmailStr


class Education(BaseModel):
    id: str
    degrees: str
    faculty: str
    major: str
    university: str
    period: str


class Project(BaseModel):
    id: int
    slug: str
    name: str
    duration: str
    description: str
    technologies: List[str]
    github: Optional[HttpUrl]
    responsibilities: List[str]
    images: List[str]


class Experience(BaseModel):
    id: int
    slug: str
    company: str
    position: str
    duration: str
    responsibilities: List[str]


class Skills(BaseModel):
    programming_languages: List[str]
    web_development: List[str]
    tools_platforms: List[str]
    methodologies: List[str]
    soft_skills: List[str]
    languages: List[str]
    
class Profile(BaseModel):
    image: str
    first_name: str
    last_name: str
    address: str
    about_me: str
    contact: Contact
    introduction: str
    education: List[Education]
    projects: List[Project]
    experiences: List[Experience]
    skills: Skills