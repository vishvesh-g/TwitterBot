from pydantic import BaseModel
from typing import List

class Twitter(BaseModel):
    title: str
    accounts: str
    accountsId: str
    