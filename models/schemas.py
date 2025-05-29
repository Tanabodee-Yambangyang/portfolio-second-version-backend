from pydantic import BaseModel

class Project(BaseModel):
    id: int
    name: str
    duration: str
    description: str
    technologies: list[str]
    github: str
    responsibilities: list[str]

class Experience(BaseModel):
    id: int
    company: str
    position: str
    duration: str
    responsibilities: list[str]