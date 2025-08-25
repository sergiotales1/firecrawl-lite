from pydantic import BaseModel

class CrawledURL(BaseModel):
    title: str
    description: str
    markdown: str
