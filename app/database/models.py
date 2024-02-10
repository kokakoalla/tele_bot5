from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import SQLALCHEMY_URL

engine = create_async_engine((SQLALCHEMY_URL, echo=True))

async_session = async_sessonmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

class Product():
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    category = relationship('Category', back_populates='products')
#    orders = relationship("Order, back_populates='product")

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all())