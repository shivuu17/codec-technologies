from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class ChatLog(Base):
    __tablename__ = 'chat_logs'

    id = Column(Integer, primary_key=True)
    user_input = Column(String)
    bot_response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
