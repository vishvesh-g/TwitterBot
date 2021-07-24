from database import Base
from sqlalchemy import Column, Integer, String

class Twitter(Base):
    __tablename__ = 'Accounts'
    
    id=Column(Integer, primary_key=True, index=True)
    title = Column(String)
    accounts = Column(String)
    accountsId = Column(String)

