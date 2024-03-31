from pydantic import BaseModel

class EmailScanRequest(BaseModel):
    email_id: str
    owner_email: str
