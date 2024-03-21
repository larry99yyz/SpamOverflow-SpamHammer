# app/models.py
from pydantic import BaseModel

class EmailScanRequest(BaseModel):
    email_id: str
