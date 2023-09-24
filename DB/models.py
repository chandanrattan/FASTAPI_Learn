from sqlalchemy import Integer, String, Boolean, Column
from DB.database import Base


class Todos(Base):
    __tablename__ = "todos"
    ##Column names are here
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
