from sqlalchemy.orm import Mapped, mapped_column
from .. import Base


class User(Base):
    __tablename__ = "users"
    
    name: Mapped[str]