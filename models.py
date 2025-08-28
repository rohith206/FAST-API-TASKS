from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Task(Base):
  __tablename__ = "tasks"


id = Column(Integer, primary_key=True, index=True)
title = Column(String(200), nullable=False, index=True)
description = Column(String(1000), nullable=True)
completed = Column(Boolean, default=False)
created_at = Column(DateTime(timezone=True), server_default=func.now())
updated_at = Column(DateTime(timezone=True), onupdate=func.now())