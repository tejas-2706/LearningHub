from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Boolean

Base = declarative_base()

class DBItem(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    is_done = Column(Boolean)





















# class User(Base):
#     __tablename__ = "users"
    
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     username: Mapped[str] = mapped_column(String, unique=True, index=True)
#     email: Mapped[str] = mapped_column(String, unique=True)


# class Campaign(Base):
#     __tablename__ = "campaign"

#     campaign_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     name: Mapped[str] = mapped_column(String, index=True)
#     due_date: Mapped[datetime] = mapped_column(datetime, default=None , index=True)
#     created_at: Mapped[datetime] = mapped_column(datetime , default_factory=lambda: datetime.now() , nullable=True, index=True)


