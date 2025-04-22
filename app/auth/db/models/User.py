from sqlalchemy import Integer, String, LargeBinary, BigInteger
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "application_user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary(64))
    salt: Mapped[bytes] = mapped_column(LargeBinary(64))
    role: Mapped[str] = mapped_column(String(30))
    tele_id: Mapped[int] = mapped_column(BigInteger, nullable=True)

    def __repr__(self) -> str:
        return f"<User {self.username}>"
